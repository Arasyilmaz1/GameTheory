
from abc import ABCMeta, abstractmethod

class Agent:
  __metaclass__ = ABCMeta

  @abstractmethod
  def policy(self, state): pass

