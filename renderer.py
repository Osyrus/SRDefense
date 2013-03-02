# The renderer class

import pygame

blueColour = pygame.Color(0, 0, 255)
redColour = pygame.Color(255, 0, 0)
greenColour = pygame.Color(0, 255, 0)
whiteColour = pygame.Color(255, 255, 255)
blackColour = pygame.Color(0, 0, 0)

class Renderer:
  """The renderer class"""

  def __init__(self, display):
    self._display = display
    self._background = whiteColour
    self._

  def setBackground(self, bg):
    self._background = bg

  def getBackground(self):
    return self._background

  def getDisplay(self):
    return self._display

  def render(self, *toDraw):

    for element in toDraw:
      element.draw(self._display)

    pygame.display.update()