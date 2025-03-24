from Agent import Agent
import sys
from Action import Action
class Human(Agent):
  def policy(self, state):
    userInput = input('Please enter your move: ')

    while True:
      try:
        userTokens = list(map(int, userInput.split(',')))
        if userInput.strip().lower() == 'quit':
          sys.exit()
        elif not state.isValid(Action(userTokens)):
          raise ValueError()
        else:
          return Action(userTokens)
      except ValueError:
        print('Oops invalid move.try again')
        userInput = input('Please enter your move: ')