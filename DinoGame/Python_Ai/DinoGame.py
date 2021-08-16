import pygame
import numpy as np
from NEAT import NEAT
import sys

PopulationSize = 1000

InToHid1 = NEAT(4, 6, MutationRate=0.1, PopulationSize=PopulationSize)
Hid1ToOut = NEAT(6, 3, MutationRate=0.1, PopulationSize=PopulationSize)

pygame.init()
pygame.display.set_caption('Dinosaur Game')

DisplayShape = (960, 540)
Display = pygame.display.set_mode([DisplayShape[0], DisplayShape[1]])

Bird = pygame.image.load('DinoGame/Python_Ai/data/Bird002.png')
Cactus = pygame.image.load('DinoGame/Python_Ai/data/Cactus001.png')
DinoDuck = pygame.image.load('DinoGame/Python_Ai/data/DinoDuck005.png')
DinoWalk = pygame.image.load('DinoGame/Python_Ai/data/DinoWalk002.png')

Alive = np.array([True] * PopulationSize, dtype=bool)
HighScore = 0
Score = np.array([0] * PopulationSize)

Gravity = 0.5
Velocity = np.array([0] * PopulationSize)
Speed = 8 # Pixels per loop

Road = np.stack((np.random.randint(0, DisplayShape[0], 100), np.random.randint(DisplayShape[1] - 20, DisplayShape[0], 100)))

ObjectShape = (73, 47)
Object = np.array([[400, 800, 1200], [DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20), DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20), DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20)]])
ObjectType = np.array(['Cactus', 'Cactus', 'Cactus'])

DinoWalkShape = np.array([40, 43])
DinoDuckShape = np.array([40, 19])
DinoShape = np.array([DinoWalkShape] * PopulationSize)
Dino = np.array([np.array([20, DisplayShape[1] - DinoWalkShape[1]])] * PopulationSize)

WHITE = (255, 255, 255)
GRAY = (83, 83, 83)
Font = pygame.font.Font('freesansbold.ttf', 20)

for Generation in range(20):
  while np.sum(Alive) != 0:
    Display.fill(WHITE)
    Display.blit(Font.render("Score: " + str(max(Score)), True, GRAY), (10, 10))
    Display.blit(Font.render("High Score: " + str(HighScore), True, GRAY), (10, 35))

    # Road
    pygame.draw.line(Display, GRAY, (0, DisplayShape[1] - 20), (DisplayShape[0], DisplayShape[1] - 20))
    for i in range(100):
      pygame.draw.rect(Display, GRAY,(Road[0, i], Road[1, i], 2, 2))
      Road[0, i] -= Speed

      if Road[0, i] <= 0:
        Road[0, i] = DisplayShape[0]
        Road[1, i] = np.random.randint(DisplayShape[1] - 20, DisplayShape[1])

    # Object
    # Display Object And Update Position
    for i in range(len(Object[0])):
      if ObjectType[i] == 'Cactus':
        Display.blit(Cactus, (Object[0, i], Object[1, i]))
      else:
        Display.blit(Bird, (Object[0, i], Object[1, i]))

      Object[0, i] -= Speed

    # Check Object Location And Posiblity Reset
    if Object[0, 0] <= -ObjectShape[0]:
      Score += 1
      Object[:, 0], ObjectType[0] = Object[:, 1], ObjectType[1]
      Object[:, 1], ObjectType[1] = Object[:, 2], ObjectType[2]
      
      Object[0, 2] = np.random.randint(1000, 1400)
      while abs(Object[0, 0] - Object[0, 1]) < 400 or abs(Object[0, 1] - Object[0, 2]) < 400 or abs(Object[0, 0] - Object[0, 2]) < 400:
        Object[0, 2] = np.random.randint(1000, 1400)
      if np.random.random_sample() <= 0.25:
        Object[1, 2] = DisplayShape[1] - (ObjectShape[1] + DinoWalkShape[1]) + np.random.randint(0, 10)
        ObjectType[i] = 'Bird'
      else:
        Object[1, 2] = DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20)
        ObjectType[i] = 'Cactus'

    # Dino
    In = np.array([Object[0, 0] - (20 + DinoWalkShape[0]), 0, Object[0, 1] - (20 + DinoWalkShape[0]), 0])
    In[1] = 0 if ObjectType[0] == 'Cactus' else 1
    In[3] = 0 if ObjectType[1] == 'Cactus' else 1
    In = np.array([In] * PopulationSize)
    Hid1 = InToHid1.ForwardProp(In)
    # Out = Hid1ToOut.ForwardProp(Hid1)
    print(Hid1.shape)
    sys.exit()
    for i in range(PopulationSize):
      if Out[i, 1] > Out[i, 0] and Out[i, 1] > Out[i, 2] and Dino[i, 1] == DisplayShape[1] - DinoShape[i, 1]: # Jump
        Velocity[i] = - 10
        DinoShape[i, :] = DinoWalkShape
      if Out[i, 2] > Out[i, 0] and Out[i, 2] > Out[i, 1] and Dino[i, 1] == DisplayShape[1] - DinoShape[i, 1]: # Duck
        DinoShape[i, :] = DinoDuckShape

      # Physics Calc
      Dino[i, 1] += Velocity[i]
      Velocity[i] += Gravity
      Dino[i, 1] = min(DisplayShape[1] - DinoShape[i, 1], max(0, Dino[i, 1]))

      # Display Dino
      if DinoShape[i, :].all() == DinoWalkShape.all():
        Display.blit(DinoWalk, (Dino[i, 0], Dino[i, 1]))
      else:
        Display.blit(DinoDuck, (Dino[i, 0], Dino[i, 1]))

      # Game Over Check
      for j in range(len(Object[0])):
        if Dino[i, 0] < Object[0, j] + ObjectShape[0] and Dino[i, 0] + DinoShape[i, 0] > Object[0, j] and Dino[i, 1] < Object[1, j] + ObjectShape[1] and Dino[i, 1] + DinoShape[i, 1] > Object[1, j]:
          Alive = False
          HighScore = max(HighScore, Score.all())
      if Dino[i, 1] == 0:
        Alive = False
        HighScore = max(HighScore, Score.all())

    pygame.display.update()

  # Mutate

  # Reset
  Score = np.array([0] * PopulationSize)
  Alive = np.array([True] * PopulationSize, dtype=bool)

  Object[0, 0] += 400
  Object[0, 1] += 400
  Object[0, 2] += 400

  DinoShape = np.array([DinoWalkShape] * PopulationSize)
  Dino = np.array([np.array([20, DisplayShape[1] - DinoWalkShape[1]])] * PopulationSize)

pygame.quit()