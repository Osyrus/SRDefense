#The building sprites group

import pygame
import renderer

class Buildings(pygame.sprite.LayeredDirty):
  """The sprite group for the buildings"""
  def __init__(self, renderer):
    super(Buildings, self).__init__()
    self.set_clip()
    
  