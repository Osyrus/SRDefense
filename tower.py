# The tower class file
import pygame
import grid
import os

class Tower(pygame.sprite.DirtySprite):
  """Base class for a tower object"""
  
  def __init__(self, pos):
    #Store it's own grid, position and aim angle
    self._pos = pos
    self._angle = 0

    #Store it's image and rectangle
    self.image = pygame.image.load(os.path.join("resources", "img", "baseSR.png"))
    self.rect = self.image.get_rect()

  def update(self, dt):
    self.dirty = 1
