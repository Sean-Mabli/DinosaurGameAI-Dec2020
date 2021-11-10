import numpy as np
import aiinpy as ai

PopulationSize = 1000

InToHid1 = ai.neuroevolution(4, 6, MutationRate=0.1, PopulationSize=PopulationSize, Activation='Identity')
Hid1ToOut = ai.neuroevolution(6, 3, MutationRate=0.1, PopulationSize=PopulationSize, Activation='Identity')

DisplayShape = (960, 540)

Alive = np.array([True] * PopulationSize, dtype=bool)
Score = np.array([0] * PopulationSize)
Velocity = np.array([0] * PopulationSize, dtype=float)

HighScore = 0
Gravity = 0.5
Speed = 8 # Pixels per loop

ObjectShape = (73, 47)
Object = np.array([[400, 800, 1200], [DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20), DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20), DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20)]])

DinoWalkShape = np.array([40, 43])
DinoDuckShape = np.array([55, 26])
DinoShape = np.array([DinoWalkShape] * PopulationSize)
Dino = np.array([np.array([20, DisplayShape[1] - DinoWalkShape[1]])] * PopulationSize)

for Generation in range(100):
  while np.sum(Alive) != 0:
    # Object
    Object[0, :] -= Speed

    if Object[0, 0] <= -ObjectShape[0]:
      for i in range (PopulationSize):
        if Alive[i]:
          Score[i] += 1
          if HighScore > Score[i]:
            HighScore = Score[i]
            print("Generation:", Generation, "New High Score:", HighScore)
        
      Object[:, 0 : 1] = Object[:, 1 : 2]
      
      Object[0, 2] = np.random.randint(1000, 1400)
      while abs(Object[0, 0] - Object[0, 1]) < 400 or abs(Object[0, 1] - Object[0, 2]) < 400 or abs(Object[0, 0] - Object[0, 2]) < 400:
        Object[0, 2] = np.random.randint(1000, 1400)
      if np.random.random_sample() <= 0.25:
        Object[1, 2] = DisplayShape[1] - (ObjectShape[1] + DinoWalkShape[1]) + np.random.randint(0, 10)
      else:
        Object[1, 2] = DisplayShape[1] - ObjectShape[1] - np.random.randint(0, 20)

    # Dino
    In = np.array([(Object[0, 0] - (20 + DinoDuckShape[0])) / 1400, 0 if Object[1, 0] < 485 else 1, (Object[0, 1] - (20 + DinoWalkShape[0])) / 1400, 0 if Object[1, 1] < 485 else 1])
    In = np.array([In] * PopulationSize)
    Hid1 = InToHid1.forwardprop(In)
    Out = Hid1ToOut.forwardprop(Hid1)

    for i in range(PopulationSize):
      if Out[i, 1] > Out[i, 0] and Out[i, 1] > Out[i, 2] and Dino[i, 1] == DisplayShape[1] - DinoShape[i, 1]: # Jump
        Velocity[i] = - 10
        DinoShape[i, :] = DinoWalkShape
      if Out[i, 2] > Out[i, 0] and Out[i, 2] > Out[i, 1] and Dino[i, 1] == DisplayShape[1] - DinoShape[i, 1]: # Duck
        DinoShape[i, :] = DinoDuckShape
        Dino[i, 1] = DisplayShape[1] - DinoDuckShape[1]

    # Physics Calc
    Dino[:, 1] += np.int64(Velocity)
    Velocity += Gravity

    for i in range(PopulationSize):
      Dino[i, 1] = min(DisplayShape[1] - DinoShape[i, 1], max(0, Dino[i, 1]))

    # Game Over Check
    for i in range(PopulationSize):
      for j in range(len(Object[0])):
        if Dino[i, 0] < Object[0, j] + ObjectShape[0] and Dino[i, 0] + DinoShape[i, 0] > Object[0, j] and Dino[i, 1] < Object[1, j] + ObjectShape[1] and Dino[i, 1] + DinoShape[i, 1] > Object[1, j]:
          Alive[i] = False

  # Mutate
  for i in range(PopulationSize):
    if Score[i] == HighScore:
      InToHid1.Mutate(i)
      Hid1ToOut.Mutate(i)
      break

  # Reset
  Score = np.array([0] * PopulationSize)
  Alive = np.array([True] * PopulationSize, dtype=bool)
  Velocity = np.array([0] * PopulationSize, dtype=float)

  Object[0, :] += 400
  
  DinoShape = np.array([DinoWalkShape] * PopulationSize)
  Dino = np.array([np.array([20, DisplayShape[1] - DinoWalkShape[1]])] * PopulationSize)