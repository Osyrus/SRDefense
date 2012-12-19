#The world grid class, stores building locations

import math

class grid:
  """The grid class, for storing and retrieving buildings within the world"""

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

  def remove(self, pos):
    if self.occupied(pos):
      #Building deleter here?
      self._locations[pos.x][pos.y] = None
    else:
      print("No building to delete!")

  def get(self, pos):
    if self.occupied(pos):
      return self._locations[pos.x][pos.y]
    else:
      print("No building to get")