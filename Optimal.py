from Agent import Agent
from Random import Random
import numpy as np
class Optimal(Agent):
  def __init__(self, randAbove = None):
    self.randAbove = randAbove
    self.Dict = {}

  def policy(self, currState):
    if self.randAbove is None:
      return self.optPolicy(currState)
    else:
      if sum(list(currState.state)) <= self.randAbove:
        return self.optPolicy(currState)
      else:
        return Random().policy(currState)
      


  def optPolicy(self, currState):
    actions = currState.getActions()
    Pactions = []
    for action in actions:
      newState = currState.peekAction(action)
      if self.rec_game(newState.state, newState.max_removal) == 'P':
        Pactions.append(action)
    if len(Pactions) == 0:
      return np.random.choice(actions)
    return np.random.choice(Pactions)
  
  def rec_game(self, lst, max_removal):
    lst = list(lst)
    if self.to_str(lst, max_removal) in self.Dict:
      return self.Dict[self.to_str(lst, max_removal)]

    if len(lst) == 0:
      self.Dict[self.to_str(lst, max_removal)] = 'P'
      return 'P'
    for pile in range(len(lst)):
      if lst[pile] >= max_removal:
        min = max_removal
      else:
        min = lst[pile]
      for removal in range(1, min + 1):
        position = lst.copy()
        position[pile] -= removal
        if position[pile] <= 0:
          position.pop(pile)
        if self.rec_game(position,2*removal) == 'P':
          self.Dict[self.to_str(lst, max_removal)] = 'N'
          return 'N'
    self.Dict[self.to_str(lst, max_removal)] = 'P'
    return 'P'
  
  # A function to turn a state of the game to a string.
  def to_str (self,lst, max_removal):
    if len(lst) == 0:
      max_val = 0
    else:
      max_val = max(lst)
    if max_val < max_removal:
      max_removal = max_val

    return str(lst)[:-1] +'; '+ str(max_removal) + ']'
  
 
  
