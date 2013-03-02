import pygame, sys
from pygame.locals import *
import tower

##Engine Setup Stuff##
#Set the resolution
res = (640, 480)
#Initialise pygame
pygame.init()
#Setup the window
display = pygame.display.set_mode(res, pygame.HWSURFACE | pygame.DOUBLEBUF)
#Set the name of the game window
pygame.display.set_caption('SRDefense Window')
#Create some simple colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Set the background colour
background = WHITE
#Create a basic font
basicFont = pygame.font.SysFont(None, 48)
#Setup the game clock object
clock = pygame.time.Clock()
#Set the loop boolean and default dt
running = True
dt = 0

##Game Related Stuff##
#Create the sprite groups to be used
tower1 = tower.Tower((100, 100))

while(running):
  #Event management
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False

    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        running = False

  #Logic stuff
  tower1.update(dt)

  #Rendering stuff
  display.fill(background)
  tower1.draw(display)

  #Update and clock tick
  pygame.display.update()
  dt = clock.tick(30)

pygame.quit()
sys.exit("Clean End")