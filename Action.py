import numpy as np
#An action of this game is just a tuple (a,b), which means remove b pebbles from ath pile.
class Action:
  def __init__(self, action):
    if type(action) is (not list or not tuple):
      raise TypeError('Argument should be a tuple or a list')
    else:
      self.action = tuple(action)

  def __str__(self):
    return '(' + str(self.action[0]) + ',' + str(self.action[1]) + ')'