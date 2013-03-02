# The tower class file
import pygame, math
import os

BLACK = (0, 0, 0)
GREY = (128, 128, 128)

class Tower():
  """Base class for a tower object"""
  
  def __init__(self, pos):
    #Store it's own position and aim angle
    self._pos = pos
    self._angle = 0
    self._type = None
    self._scale = 100
    self._splitSize = 25

    self._innerAng = 0
    self._innerSpeedMax = 50
    self._innerSpeed = 0

    self._maxEnergy = 100
    self._energy = 0
    self._chargeRate = 1

  def update(self, dt):
    #Spin the inner ring
    if (self._innerAng + self._innerSpeed) < 360:
      self._innerAng = self._innerAng + self._innerSpeed
    else:
      self._innerAng = self._innerSpeed - (360 - self._innerAng)

    #Charge the towers energy storage
    if (self._energy + self._chargeRate) < self._maxEnergy:
      self._energy = self._energy + self._chargeRate
    else:
      self._energy = self._maxEnergy

    #Set the inner ring speed relative to energy storage
    self._innerSpeed = self._innerSpeedMax * (self._energy / float(self._maxEnergy))

  def draw(self, display):
    #Create the base rectangle of the tower
    baseRect = pygame.Rect(self._pos[0]-self._scale/2,self._pos[1]-self._scale/2,self._scale,self._scale)
    #Draw the base
    pygame.draw.rect(display, GREY, baseRect)
    #Draw the outer ring
    startAng = toRad(self._angle + self._splitSize/2)
    endAng = toRad(self._angle + (360 - self._splitSize/2))
    pygame.draw.arc(display, BLACK, baseRect, startAng, endAng, self._scale/7)
    #Create the base rectangle of the inner ring
    innerRect = pygame.Rect(self._pos[0]-self._scale/4,self._pos[1]-self._scale/4,self._scale/2,self._scale/2)
    #Draw the inner ring
    startAng = toRad(self._innerAng + self._splitSize/2)
    endAng = toRad(self._innerAng + (360 - self._splitSize/2))
    pygame.draw.arc(display, BLACK, innerRect, startAng, endAng, self._scale/10)

def toRad(deg):
  return deg * math.pi / 180.0
