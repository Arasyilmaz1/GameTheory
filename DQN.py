import numpy as np
import random
from operator import itemgetter
import tensorflow as tf
from tensorflow import keras
from keras import layers
from collections import deque
from Agent import Agent
from State import State

class DQN(Agent):
  def __init__(self,max_pebbles, max_piles, epsilon,alpha=5e-4,gamma=0.99, buffer_size=10000, batch_size = 64):
    self.epsilon = epsilon
    self.alpha = alpha
    self.gamma = gamma
    self.max_pebbles = max_pebbles
    self.max_piles = max_piles


    self.model = DQN._create_q_model(max_pebbles,max_piles)
    self.model_target = DQN._create_q_model(max_pebbles,max_piles)
    self.replay_buffer = deque(maxlen=buffer_size)
    self.batch_size = batch_size

    self.loss_function = keras.losses.Huber(delta=1)
    self.optimizer = keras.optimizers.Adam(learning_rate=alpha)
    self.cum_loss = 0

  def _create_q_model(max_pebbles,max_piles):
    inputs = layers.Input(shape= (max_piles,max_pebbles.bit_length()))
    layer0 = layers.Flatten(input_shape=(3, 3), name="flatten")(inputs)
    layer1 = layers.Dense(128, activation="relu", name="dense_1")(layer0)
    layer2 = layers.Dense(128, activation="relu", name="dense_2")(layer1)
    action = layers.Dense(max_pebbles*max_piles,activation='linear', name= "output_linear")(layer2)
    return keras.Model(inputs=inputs, outputs=action)

  def _decode_state(state_converted):
    lst = []
    for i in range(len(state_converted)-1):
      num = 0
      for j in range(len(state_converted[i])):
        if state_converted[i][j]:
          num += 2**j
      lst.append(num)
    return lst
  
  def _encode_heaps(self,heaps):
    tensor_size = max(max(heaps).bit_length(),len(heaps))
    square =[]
    for heap in heaps:
      representation = bin(heap)[-1:1:-1]
      lst = [char == '1' for char in representation]
      while len(lst) < tensor_size:
        lst.append(False)
      square.append(lst)
    while len(square) < tensor_size:
      square.append([False]*tensor_size)
    return tf.convert_to_tensor(square)

  def get_qvalues(self, heaps):
    qvalues = self.model(
        tf.expand_dims(self._encode_heaps(heaps), axis=0),
        training=False
        )
    return qvalues[0]

  def _pick_best_move(self, heaps, max_removal):
    qvls = self.get_qvalues(heaps)
    qvls_possible = qvls.numpy()
    for i in range(len(qvls)):
      if i%self.max_pebbles+1 > max_removal or i%self.max_pebbles+1 > heaps[i//self.max_pebbles]:
        qvls_possible[i] = -1
    qvalues_indexed = [(i,qvl) for i, qvl in enumerate(qvls_possible)]
    random.shuffle(qvalues_indexed)
    max_index = max(qvalues_indexed, key=itemgetter(1))[0]
    return qvls_possible[max_index], (max_index //self.max_pebbles+1, max_index % self.max_pebbles +1)

  def get_max_qvalue(self, heaps):
    best_value, best_move = self._pick_best_move(heaps)
    return best_value

  def act(self, state):
    if random.random() < self.epsilon:
      move = random.choice(state.getActions())
    else: 
      move = self._pick_best_move(state.state, state.max_removal)[1]
    return move
  
  def on_step(self, state, action, reward, next_state, debug):
    internal_action = (action[0]-1)*self.max_pebbles+(action[1]-1)
    self.replay_buffer.append((

      self._encode_heaps(state.state),
      internal_action,
      reward,
      self._encode_heaps(next_state.state)
    ))
    if len(self.replay_buffer) < self.batch_size:
      return 
    minibatch_indices = np.random.choice(len(self.replay_buffer), size=self.batch_size)
    minibatch = [self.replay_buffer[i] for i in minibatch_indices]
    minibatch_states = np.array([prev[0] for prev in minibatch])
    minibatch_actions = [prev[1] for prev in minibatch]
    minibatch_rewards = [prev[2] for prev in minibatch]
    minibatch_next_states = np.array([prev[3] for prev in minibatch])

        # Compute target
    target_q_values = self.model_target(minibatch_next_states) * np.any(minibatch_next_states, axis=(1, 2)).astype(int)[:, None]
    target_term = minibatch_rewards + self.gamma * tf.reduce_max(
        target_q_values,
        axis=1
        )
    mask = tf.one_hot(minibatch_actions, self.max_pebbles*self.max_piles)
    with tf.GradientTape() as tape:
            q_values = self.model(minibatch_states)
            q_action = tf.reduce_sum(tf.multiply(q_values, mask), axis=1)
            loss = self.loss_function(target_term, q_action)
    self.cum_loss += loss
    grads = tape.gradient(loss, self.model.trainable_variables)
    self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))

  def update_target(self):
        self.model_target.set_weights(self.model.get_weights())
  
         
