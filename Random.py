from Agent import Agent
import numpy as np
class Random(Agent):
  def policy(self, state):
    return np.random.choice(state.getActions())