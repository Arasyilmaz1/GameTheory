import numpy as np
import random
from operator import itemgetter
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from collections import deque
from Agent import Agent
from State import State

class DQN(Agent):
  def __init__(self,max_pebbles, max_piles, epsilon,alpha=5e-4,gamma=0.99, buffer_size=10000, batch_size = 64):
    self.epsilon = epsilon
    self.alpha = alpha
    self.gamma = gamma


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
    action = layers.Dense(21,activation='linear', output= "output_linear")(layer2)
    return keras.Model(inputs=inputs, outputs=action)

  def _decode_state(self,state_converted):
    lst = []
    for i in range(len(state_converted)-1):
      num = 0
      for j in range(len(state_converted[i])):
        if state_converted[i][j]:
          num += 2**j
      lst.append(num)

    max_removal = 0
    for i in range(state_converted[-1]):
      max_removal += 2**i*int(state_converted[-1][i])

    return State(lst, max_removal)
