import pygame
import numpy as np
from NEAT import NEAT
import time

InToHid1 = NEAT(4, 6, MutationRate=0.1, PopulationSize=1000)
Hid1ToOut = NEAT(6, 3, MutationRate=0.1, PopulationSize=1000)

pygame.init()
pygame.display.set_caption('Dinosaur Game')

DisplayShape = (960, 540)
Display = pygame.display.set_mode([DisplayShape[0], DisplayShape[1]])

Bird = pygame.image.load('DinoGame\Python_Ai\data\Bird002.png')
Cactus = pygame.image.load('DinoGame\Python_Ai\data\Cactus001.png')
DinoDuck = pygame.image.load('DinoGame\Python_Ai\data\DinoDuck004.png')
DinoWalk = pygame.image.load('DinoGame\Python_Ai\data\DinoWalk002.png')

Alive = np.array([True] * 1000, dtype=bool)
HighScore = 0
Score = np.array([0] * 1000)

Gravity = 0.5
Velocity = 0
Speed = 8 # Pixels per loop

Road = np.stack((np.random.randint(0, DisplayShape[0], 100), np.random.randint(DisplayShape[1] - 20, DisplayShape[0], 100)))

ObjectShape = (73, 47)
Object = np.array([[1000, 1400, 1800], [DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20), DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20), DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20)]])
ObjectType = np.array(['Cactus', 'Cactus', 'Cactus'])

DinoShape = (40, 43)
Dino = np.array([20, DisplayShape[1] - DinoShape[1]])
DinoType = 'Walk'

WHITE = (255, 255, 255)
GRAY = (83, 83, 83)

for Generation in range(100):
  while np.sum(Alive) != 0:
    Display.fill(WHITE)
    Display.blit(pygame.font.SysFont("Raleway", 40).render("Score: " + str(Score), 1, GRAY), (750, 10))
    Display.blit(pygame.font.SysFont("Raleway", 40).render("High Score: " + str(HighScore), 1, GRAY), (750, 40))
    time.sleep(0.01)

    # Road
    pygame.draw.line(Display, GRAY, (0, DisplayShape[1] - 20), (DisplayShape[0], DisplayShape[1] - 20))
    for i in range(100):
      pygame.draw.rect(Display, GRAY,(Road[0, i], Road[1, i], 2, 2))
      Road[0, i] -= Speed

      if Road[0, i] <= 0:
        Road[0, i] = DisplayShape[0]
        Road[1, i] = np.random.randint(DisplayShape[1] - 20, DisplayShape[1])

    # Object
    for i in range(len(Object[0])):
      if ObjectType[i] == 'Cactus':
        Display.blit(Cactus, (Object[0, i], Object[1, i]))
      else:
        Display.blit(Bird, (Object[0, i], Object[1, i]))

      Object[0, i] -= Speed

    if Object[0, 0] <= -ObjectShape[0]:
      Score += 1
      Object[:, 0], ObjectType[0] = Object[:, 1], ObjectType[1]
      Object[:, 1], ObjectType[1] = Object[:, 2], ObjectType[2]
      
      Object[0, 2] = np.random.randint(1000, 1400)
      while abs(Object[0, 0] - Object[0, 1]) < 400 or abs(Object[0, 1] - Object[0, 2]) < 400 or abs(Object[0, 0] - Object[0, 2]) < 400:
        Object[0, 2] = np.random.randint(1000, 1400)
      if np.random.random_sample() <= 0.2:
        Object[1, 2] = DisplayShape[1] - (ObjectShape[1] + DinoShape[1]) + np.random.randint(0, 10)
        ObjectType[i] = 'Bird'
      else:
        Object[1, 2] = DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20)
        ObjectType[i] = 'Cactus'

    # Dino
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and Dino[1] == DisplayShape[1] - DinoShape[1]:
          Velocity = - 10
          DinoShape = (40, 43)
          DinoType = 'Walk'
        if event.key == pygame.K_DOWN and Dino[1] == DisplayShape[1] - DinoShape[1]:
          DinoShape = (55, 26)
          DinoType = 'Duck'

    Dino[1] += Velocity
    Velocity += Gravity
    Dino[1] = min(DisplayShape[1] - DinoShape[1], max(0, Dino[1]))

    if DinoType == 'Walk':
      Display.blit(DinoWalk, (Dino[0], Dino[1]))
    else:
      Display.blit(DinoDuck, (Dino[0], Dino[1]))

    # Game Over Check
    for i in range(len(Object[0])):
      if Dino[0] < Object[0, i] + ObjectShape[0] and Dino[0] + DinoShape[0] > Object[0, i] and Dino[1] < Object[1, i] + ObjectShape[1] and Dino[1] + DinoShape[1] > Object[1, i]:
        Alive = False
        HighScore = max(HighScore, Score)
    if Dino[1] == 0:
      Alive = False
      HighScore = max(HighScore, Score)

    pygame.display.update()

  # Reset
  Score = 0
  Alive = True

  Object[0, 0] += 400
  Object[0, 1] += 400
  Object[0, 2] += 400

  DinoShape = (40, 43)
  Dino = np.array([20, DisplayShape[1] - DinoShape[1]])
  DinoType = 'Walk'

pygame.quit()