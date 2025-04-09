# A state in this game is a list together with a number max_removal. List represents the number of pebbles left in each pile.
# max_removal represents the maximum number of pebbles that can be removed from a pile.
from Action import Action
class State:
  def __init__(self, state, max_removal):
    if type(state) is (not list or not tuple):
      raise TypeError('state should be a list')
    elif max_removal < 0 or type(max_removal) is not int:
      raise TypeError('max removal should be an nonnegative integer')
    else:
      self.state = tuple(state)
      self.max_removal = max_removal
      self.num_acts = 0
  def isTerminal(self):
    return sum(self.state) == 0

  def __str__ (self):

    if len(self.state) == 0:
      max_val = 0
    else:
      max_val = max(self.state)
    if max_val < self.max_removal:
      self.max_removal = max_val

    return str(self.state)[:-1] +'; '+ str(self.max_removal) + ']'

  def getActions(self):
    if self.isTerminal():
      return [None]
    else:
      return [Action([i,j]) for i in range(len(self.state)) for j in range(1,min(self.max_removal+1,self.state[i]+1))]

  def doAction(self, action):
    if action is not None:
      self.state = list(self.state)
      if self.state[action.action[0]] >= action.action[1]:
        self.state[action.action[0]] -= action.action[1]
        self.max_removal = 2*action.action[1]
      else:
        self.max_removal = 2*self.state[action.action[0]]
        self.state[action.action[0]] = 0
      self.state = tuple(self.state)
      self.num_acts += 1

  def peekAction(self,action):
    newState = State(list(self.state), self.max_removal)
    newState.doAction(action)
    return newState

  def isValid(self, action):
    if action is None:
      return False
    elif action.action[0] < 0 or action.action[0] >= len(self.state):
      return False
    elif action.action[1] < 1 or action.action[1] > self.max_removal:
      return False
    return True
