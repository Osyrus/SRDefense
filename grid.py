#The world grid class, stores building locations

import math

class grid:
  """docstring for grid"""

  def __init__(self, size):
    #Create the two dimension matrix to store references to buildings in
    self._locations = [[None for x in xrange(size.y)] for x in xrange(size.x)]
    #Store the size of the grid
    self._size = size

  def toGrid(pos):
    _gridPos = dict()

    #Calculate the grid coordinate from the absolute coordinate
    _gridPos.x = math.floor(pos.x)
    _gridPos.y = math.floor(pos.y)

    return _gridPos

  def occupied(self, pos):
    if not self._locations[pos.x][pos.y]:
      return False
    else:
      return True

  def add(self, pos, building):
    if not self.occupied(pos):
      self._locations[pos.x][pos.y] = building
    else:
      print("Cannot place building, grid position occupied")