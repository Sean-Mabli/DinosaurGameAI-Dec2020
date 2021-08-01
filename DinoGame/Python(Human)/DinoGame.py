import pygame
import numpy as np
import time

Bird = pygame.image.load('DinoGame\Python(Human)\data\Bird002.png')
Cactus = pygame.image.load('DinoGame\Python(Human)\data\Cactus001.png')
DinoDuck = pygame.image.load('DinoGame\Python(Human)\data\DinoDuck004.png')
DinoWalk = pygame.image.load('DinoGame\Python(Human)\data\DinoWalk002.png')

Alive = True
HighScore = 0

ScreenShape = (960, 540)
DinoShape = (40, 43)
Dino = (20, ScreenShape[1] - DinoShape[1])
ObjectShape = (73, 47)

Gravity = 0.65
Speed = 8 # Pixels per loop
Velocity = 0
HighScore = 0

Object = np.array([[1000, 1400, 1800], [ScreenShape[1] - ObjectShape[1] - np.random.randint(0, 20), ScreenShape[1] - ObjectShape[1] - np.random.randint(0, 20), ScreenShape[1] - ObjectShape[1] - np.random.randint(0, 20)]])
ObjectType = np.array(['Cactus', 'Cactus', 'Cactus'])

Road = np.stack((np.random.randint(0, ScreenShape[0], 100), np.random.randint(ScreenShape[1] - 20, ScreenShape[0], 100)))

WHITE = (255, 255, 255)
GRAY = (83, 83, 83)

pygame.init()
pygame.display.set_caption('Dinosaur Game')

Display = pygame.display.set_mode([ScreenShape[0], ScreenShape[1]])

def DisplayGame():
  Display.fill(WHITE)

  # Road
  pygame.draw.line(Display, GRAY, (0, ScreenShape[1] - 20), (ScreenShape[0], ScreenShape[1] - 20))
  for i in range(100):
    pygame.draw.rect(Display, GRAY,(Road[0, i], Road[1, i], 2, 2))
    Road[0, i] -= 1 # Score

    if Road[0, i] <= 0:
      Road[0, i] = ScreenShape[0]
      Road[1, i] = np.random.randint(ScreenShape[1] - 20, ScreenShape[1])

  # Object
  for i in range(len(Object[0])):
    if ObjectType[i] == 'Cactus':
      Display.blit(Cactus, (Object[0, i], Object[1, i]))
    else:
      Display.blit(Bird, (Object[0, i], Object[1, i]))

    Object[0, i] -= 1 # Score

    if Object[0, i] <= 0:
      Object[0, i] = np.random.randint(1000, 1400)
      while abs(Object[0, 0] - Object[0, 1]) < 300 or abs(Object[0, 1] - Object[0, 2]) < 300 or abs(Object[0, 0] - Object[0, 2]) < 300:
        Object[0, i] = np.random.randint(1000, 1400)
      if np.random.random_sample() <= 0.2:
        Object[1, i] = ScreenShape[1] - (ObjectShape[1] + DinoShape[1]) - np.random.randint(0, 10)
        ObjectType[i] = 'Bird'
      else:
        Object[1, i] = ScreenShape[1] - ObjectShape[1] - np.random.randint(0, 20)
        ObjectType[i] = 'Cactus'

  # Dino
  Display.blit(DinoWalk, (Dino[0], Dino[1]))
  
  pygame.display.update()

def GameOver():
  for i in range(len(Object[0])):
    if Dino[0] < Object[0, i] + ObjectShape[0] and Dino[0] + DinoShape[0] > Object[0, i] and Dino[1] < Object[1, i] + ObjectShape[1] and Dino[1] + DinoShape[1] > Object[1, i]:
      Alive = False
      # HighScore = max(HighScore, Score)
      time.sleep(10)

while Alive == True:
  DisplayGame()
  GameOver()

pygame.quit()