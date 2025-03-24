import numpy as np

# A function to turn a state of the game to a string.
def to_str (lst, max_removal):

  if len(lst) == 0:
    max_val = 0
  else:
    max_val = max(lst)
  if max_val < max_removal:
    max_removal = max_val

  return str(lst)[:-1] +'; '+ str(max_removal) + ']'

# This function recursively calculates the outcome of a position in a given state.
def rec_game(Dict, lst, max_removal):
  lst = list(lst)
  if to_str(lst, max_removal) in Dict:
    return Dict[to_str(lst, max_removal)]

  if len(lst) == 0:
    Dict[to_str(lst, max_removal)] = 'P'
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
      if rec_game(Dict, position,2*removal) == 'P':
        Dict[to_str(lst, max_removal)] = 'N'
        return 'N'
  Dict[to_str(lst, max_removal)] = 'P'
  return 'P'