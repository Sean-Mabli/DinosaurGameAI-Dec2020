import pygame
import numpy as np
import time

Object = np.zeros((3, 2))
ObjectType = np.zeros(3)
Width, Height = 960, 540
Road = np.stack((np.random.randint(0, Width, (100)), np.random.randint(Height - 20, Height, (100))))
ObjectShape = (73, 47)
Gravity = 0.65
Speed = 8 # Pixels per loop
HighScore = 0

WHITE = (255, 255, 255)
GRAY = (83, 83, 83)

pygame.init()
pygame.display.set_caption('Dinosaur Game')

Display = pygame.display.set_mode([Width, Height])



while True:
  Display.fill(WHITE)
  for i in range(100): 
    pygame.draw.rect(Display, GRAY,(Road[0, i], Road[1, i], 2, 2))
    Road[0, i] -= 1
    if Road[0, i] <= 0:
      Road[0, i] = Width
      Road[1, i] = np.random.randint(Height - 20, Height)
  pygame.display.update()
  
pygame.quit()