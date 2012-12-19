import pygame
import sys
from pygame.locals import *

import tower

blueColour = pygame.Color(0, 0, 255)
redColour = pygame.Color(255, 0, 0)
greenColour = pygame.Color(0, 255, 0)
whiteColour = pygame.Color(255, 255, 255)
blackColour = pygame.Color(0, 0, 0)

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

  def loopEvent(self, event):
    if event.type == pygame.QUIT:
      self._running = False

    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        self._running = False

    if event.type == MOUSEBUTTONUP:
      if event.button == 1:
        pass

      if event.button == 3:
        pass

    if event.type == MOUSEBUTTONDOWN:
      if event.button == 1:
        pass

  def loopLogic(self):
    pass

  def loopRender(self):
    self._display.fill(whiteColour)


  def loopEnd(self):
    pygame.quit()
    sys.exit("Goodbye")

  def runLoop(self):
    if self._running == False:
      self.init()

    while(self._running):
      for event in pygame.event.get():
        self.loopEvent(event)

      self.loopLogic()

      self.loopRender()

      pygame.display.update()
      self._clock.tick(30)

    self.loopEnd()

if __name__ == "__main__":
  window = Window()
  window.runLoop()