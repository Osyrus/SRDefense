#The world grid class, stores building locations

import math
import buildings

class Grid:
  """The grid class, for storing and retrieving buildings within the world"""

  def __init__(self, size, renderer):
    #Create the two dimension matrix to store references to buildings in
    self._locations = [[None for x in xrange(size['y'])] for x in xrange(size['x'])]
    #Store the size of the grid
    self._size = size
    #Create the sprite group for the buildings
    self._buildingGroup = buildings.Buildings(renderer)
    #Scaling factor for the grid coords
    self._gridScale = 20

  def toGrid(self, pos):
    return {'x': int(math.floor(pos[0]/self._gridScale)), 'y': int(math.floor(pos[1]/self._gridScale))}

  def occupied(self, pos):
    if not self._locations[int(pos['x'])][int(pos['y'])]:
      return False
    else:
      return True

  def add(self, pos, building):
    if not self.occupied(pos):
      self._locations[int(pos['x'])][int(pos['y'])] = building
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

  def draw(self, surface):
    self._buildingGroup.draw(surface)

  def update(self, dt):
    self._buildingGroup.update(dt)