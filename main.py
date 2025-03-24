

import optuna
from State import State
from QLearning import Q_Learning
from Optimal import Optimal
from Nim import Nim
import numpy as np
import matplotlib.pyplot as plt

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
