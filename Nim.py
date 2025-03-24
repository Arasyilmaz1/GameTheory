import numpy as np
from State import State 
from QLearning import Q_Learning
from Human import Human
from Optimal import Optimal
from rec_game import rec_game

class Nim:
  def __init__(self, player1, player2, nGames):
    self.player1 = player1
    self.player2 = player2
    self.nGames = nGames
    self.prop_list = []
    self.wins = 0
    self.losses = 0
    self.num_correct_actions = 0
    self.num_actions = 0
    self.Dict = {}

  def isCorrect(self, action, currState):
    if rec_game(self.Dict, currState.state, currState.max_removal) == 'P':
      return True
    elif rec_game(self.Dict, currState.peekAction(action).state, currState.peekAction(action).max_removal) == 'P':
      return True
    else:
      return False




  def play(self, initState, eps_decay):
    for i in np.arange(self.nGames):
      currState = State(initState.state, initState.max_removal)

      if eps_decay and type(self.player1) is Q_Learning:
        self.player1.updateEps(i)
      if eps_decay and type(self.player2) is Q_Learning:
        self.player2.updateEps(i)

      if type(self.player1) is Human or type(self.player2) is Human:
        print('Starting state: ' + str(currState))
      while True:
        if type(self.player1) is Q_Learning:
          action_p1 = self.player1.updateQ(currState)
        else:
          action_p1 = self.player1.policy(currState)
        if self.isCorrect(action_p1,currState):
          self.num_correct_actions += 1
        self.num_actions += 1
        currState.doAction(action_p1)
        if type(self.player1) is Human or type(self.player2) is Human:
          print(action_p1)
          print(currState)
        if action_p1 is None:
          self.losses += 1
          break
        elif currState.isTerminal():
          self.wins += 1
          break
        if type(self.player2) is Q_Learning:
          action_p2 = self.player2.updateQ(currState)
        else:
          action_p2 = self.player2.policy(currState)
        currState.doAction(action_p2)
        if type(self.player1) is Human or type(self.player2) is Human:
          print(action_p2)
          print(currState)
      self.prop_list.append(self.num_correct_actions/self.num_actions)