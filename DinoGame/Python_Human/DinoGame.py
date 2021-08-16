import pygame
import numpy as np
import time

pygame.init()
pygame.display.set_caption('Dinosaur Game')

ScreenShape = (960, 540)
Display = pygame.display.set_mode([ScreenShape[0], ScreenShape[1]])

Bird = pygame.image.load('DinoGame\Python_Human\data\Bird002.png')
Cactus = pygame.image.load('DinoGame\Python_Human\data\Cactus001.png')
DinoDuck = pygame.image.load('DinoGame\Python_Human\data\DinoDuck004.png')
DinoWalk = pygame.image.load('DinoGame\Python_Human\data\DinoWalk002.png')

Alive = True
HighScore = 0
Score = 0

Gravity = 0.5
Speed = 8 # Pixels per loop
Velocity = 0

Road = np.stack((np.random.randint(0, ScreenShape[0], 100), np.random.randint(ScreenShape[1] - 20, ScreenShape[0], 100)))

ObjectShape = (73, 47)
Object = np.array([[1000, 1400, 1800], [ScreenShape[1] - ObjectShape[1] - np.random.randint(0, 20), ScreenShape[1] - ObjectShape[1] - np.random.randint(0, 20), ScreenShape[1] - ObjectShape[1] - np.random.randint(0, 20)]])
ObjectType = np.array(['Cactus', 'Cactus', 'Cactus'])

DinoShape = (40, 43)
Dino = np.array([20, ScreenShape[1] - DinoShape[1]])
DinoType = 'Walk'

WHITE = (255, 255, 255)
GRAY = (83, 83, 83)

for _ in range(20):
  while Alive:
    Display.fill(WHITE)
    Display.blit(pygame.font.SysFont("Raleway", 40).render("Score: " + str(Score), 1, GRAY), (750, 10))
    Display.blit(pygame.font.SysFont("Raleway", 40).render("High Score: " + str(HighScore), 1, GRAY), (750, 40))
    time.sleep(0.01)

    # Road
    pygame.draw.line(Display, GRAY, (0, ScreenShape[1] - 20), (ScreenShape[0], ScreenShape[1] - 20))
    for i in range(100):
      pygame.draw.rect(Display, GRAY,(Road[0, i], Road[1, i], 2, 2))
      Road[0, i] -= Speed

      if Road[0, i] <= 0:
        Road[0, i] = ScreenShape[0]
        Road[1, i] = np.random.randint(ScreenShape[1] - 20, ScreenShape[1])

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
        Object[1, 2] = ScreenShape[1] - (ObjectShape[1] + DinoShape[1]) + np.random.randint(0, 10)
        ObjectType[i] = 'Bird'
      else:
        Object[1, 2] = ScreenShape[1] - ObjectShape[1] - np.random.randint(0, 20)
        ObjectType[i] = 'Cactus'

    # Dino
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and Dino[1] == ScreenShape[1] - DinoShape[1]:
          Velocity = - 10
          DinoShape = (40, 43)
          DinoType = 'Walk'
        if event.key == pygame.K_DOWN and Dino[1] == ScreenShape[1] - DinoShape[1]:
          DinoShape = (55, 26)
          DinoType = 'Duck'

    Dino[1] += Velocity
    Velocity += Gravity
    Dino[1] = min(ScreenShape[1] - DinoShape[1], max(0, Dino[1]))

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

  Object[0, 0] += 1000
  Object[0, 1] += 1000
  Object[0, 2] += 1000

  DinoShape = (40, 43)
  Dino = np.array([20, ScreenShape[1] - DinoShape[1]])
  DinoType = 'Walk'

pygame.quit()