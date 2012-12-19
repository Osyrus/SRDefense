import pygame
import sys
from pygame.locals import *

from tower import *
from renderer import *
from grid import *

class Window:
  def __init__(self, width = 640, height = 400):
    self.size = self.width, self.height = width, height
    self._display = None
    self._running = False

  def init(self):
    pygame.init()
    self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    self._running = True
    self._clock = pygame.time.Clock()
    self._renderer = Renderer(self._display)
    self._grid = Grid({'x': 20, 'y': 20}, self._renderer)

  def loopEvent(self, event):
    if event.type == pygame.QUIT:
      self._running = False

    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        self._running = False

    if event.type == MOUSEBUTTONUP:
      if event.button == 1:
        addTower(self._grid, event.pos)

      if event.button == 3:
        pass

    if event.type == MOUSEBUTTONDOWN:
      if event.button == 1:
        pass

  def loopLogic(self, dt):
    self._grid.update(dt)

  def loopEnd(self):
    pygame.quit()
    sys.exit("Goodbye")

  def runLoop(self):
    if self._running == False:
      self.init()

    _dt = 0

    addTower(self._grid, (1.5, 2.5))

    while(self._running):
      for event in pygame.event.get():
        self.loopEvent(event)

      self.loopLogic(_dt)

      self._renderer.render(self._grid)

      _dt = self._clock.tick(30)

    self.loopEnd()

def addTower(grid, pos):
  #Find the grid coordinate
  print("Mouse location: " + str(pos))
  gridPos = grid.toGrid(pos)
  print("Grid location: " + str(gridPos))

  if not grid.occupied(gridPos):
    #Create a tower
    tower = Tower(gridPos)
    #Add the tower to the grid
    grid.add(gridPos, tower)
  else:
    print("Cannot add tower, grid position occupied")

if __name__ == "__main__":
  window = Window()
  window.runLoop()