# The renderer class

class Renderer:
  """The renderer class"""

  def __init__(self):
    self._background = whiteColour

  def setBackground(self, bg):
    self._background = bg

  def render(self, dt, *toDraw):
    self._display.fill(self._background)

    for element in toDraw:
      element.draw()

    pygame.display.update()