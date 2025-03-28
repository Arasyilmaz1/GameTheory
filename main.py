

import optuna
from State import State
from QLearning import Q_Learning
from Optimal import Optimal
from Nim import Nim
import numpy as np
import matplotlib.pyplot as plt
from DQN import DQN


DQNAgent = DQN(5,3,0.01)
opt = Optimal()
DQN_vs_Opt = Nim(DQNAgent, opt, 10000)
DQN_vs_Opt.play(State([4,3,2],3), False)


def objective(trial):
  alpha = trial.suggest_float('alpha', 0.0, 1.0)
  gamma = trial.suggest_float('gamma', 0.0, 1.0)
  multiplier = trial.suggest_float('multiplier',0.9,0.9999)
  decay_slowness = trial.suggest_int('decay_slowness', 1, 1000)

  qAgent = Q_Learning(alpha, gamma, 1, 0.01, multiplier, decay_slowness)
  optAgent = Optimal()
  qAgent_vs_opt = Nim(qAgent, optAgent, 200000)
  qAgent_vs_opt.play(State([1,2,3,4,5],5), True)

  print('Wins: ',qAgent_vs_opt.wins,' Losses: ',qAgent_vs_opt.losses, ' Correct Actions: ', qAgent_vs_opt.num_correct_actions,' Total Actions: ', qAgent_vs_opt.num_actions)
  plt.plot(qAgent_vs_opt.prop_list)
  return np.mean(np.array(qAgent_vs_opt.prop_list[-100:-1]))


study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=20)


DQNagent = DQN(5,3,0)
optAgent = Optimal()
DQN_vs_opt = Nim(DQNagent, optAgent, 2000)


def play(initState):
    for i in np.arange(DQN_vs_opt.nGames):
      currState = State(initState.state, initState.max_removal)
      total_reward = 0
      while True:
        action_p1 = DQN_vs_opt.player1.act(currState)
        next_state = currState.peekAction(Action((action_p1[0]-1,action_p1[1])))

        if DQN_vs_opt.isCorrect(Action((action_p1[0]-1,action_p1[1])),currState):
          DQN_vs_opt.num_correct_actions += 1
        DQN_vs_opt.num_actions += 1
        reward = 0

        if action_p1 is None:
          DQN_vs_opt.losses += 1
          reward = -1
          break
        elif currState.isTerminal():
          DQN_vs_opt.wins += 1
          reward = 1
          break
        DQN_vs_opt.player1.on_step(currState, action_p1, reward, next_state, debug=False)
        total_reward += reward
        currState.doAction(Action((action_p1[0]-1,action_p1[1])))
        if type(DQN_vs_opt.player2) is Q_Learning:
          action_p2 = DQN_vs_opt.player2.updateQ(currState)
        else:
          action_p2 = DQN_vs_opt.player2.policy(currState)
        currState.doAction(action_p2)
      DQN_vs_opt.prop_list.append(DQN_vs_opt.num_correct_actions/DQN_vs_opt.num_actions)
      if i % 100 == 0:
        DQN_vs_opt.player1.update_target()
      print(f"Episode {i+1}/{DQN_vs_opt.nGames} - Total Reward: {total_reward}")

play(State([5,4,2],5))