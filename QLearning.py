from Agent import Agent
import numpy as np
from State import State
class Q_Learning(Agent):

  prevState = prevAction = None
  WIN_REWARD, LOSS_REWARD = 1.0, -1.0

  def __init__(self, alpha, gamma, epsilon, min_eps, multiplier, decay_slowness):
    self.alpha = alpha
    self.gamma = gamma
    self.epsilon = epsilon
    self.multiplier = multiplier
    self.decay_slowness = decay_slowness
    self.min_eps = min_eps
    self.Q = {}

  def makeKey(self, currState):
    possActions = currState.getActions()
    someAction = possActions[0].action
    currState_tuple = (tuple(currState.state),currState.max_removal)

    if (currState_tuple,someAction) not in self.Q:
      for i in possActions:
        self.Q[(currState_tuple,i.action)] = np.random.uniform(0.0,0.01)

  def policy(self, currState):
    possActions = currState.getActions()
    currState_tuple = (tuple(currState.state),currState.max_removal)
    if np.random.random() > self.epsilon:
      qVal = [self.Q[(currState_tuple, a.action)]for a in possActions]
      return possActions[np.argmax(qVal)]
    else:
      return np.random.choice(possActions)

  def updateQ(self, currState):
    if currState.isTerminal():
      prevState_tuple = (tuple(self.prevState.state),self.prevState.max_removal)
      self.Q[(prevState_tuple,self.prevAction.action)] += self.alpha*(self.LOSS_REWARD - self.Q[(prevState_tuple,self.prevAction.action)])
      currAction = self.prevState = self.prevAction = None
    else:
      self.makeKey(currState)
      currAction = self.policy(currState)


      if self.prevAction is not None:
        currState_tuple = (tuple(currState.state),currState.max_removal)
        nextState = currState.peekAction(currAction)
        reward = 0 if not nextState.isTerminal() else self.WIN_REWARD
        maxQ = max([self.Q[(currState_tuple,a.action)] for a in currState.getActions()])
        prevState_tuple = (tuple(self.prevState.state),self.prevState.max_removal)

        self.Q[(prevState_tuple,self.prevAction.action)] += self.alpha*(reward+(self.gamma*maxQ) -
        self.Q[(prevState_tuple,self.prevAction.action)])
      self.prevState, self.prevAction = State(currState.state,currState.max_removal), currAction
    return currAction

  def updateEps(self, i):
    self.epsilon = max(self.min_eps,self.multiplier**(i/self.decay_slowness))