import numpy as np
from NEAT import NEAT

PopulationSize = 1000

ObjectType = np.array(2)
ObjectLocation = np.array((2, 2))
ObjectShape = (80, 60)

Gravity = 0.65
Speed = 8

MutationRate = 0.1

DinoShape = np.array([60, 40] * PopulationSize)
DinoScore = np.array([0] * PopulationSize)
HighScore = 0

DinoAlive = np.array([True] * PopulationSize, dtype=bool)

InToHid1 = NEAT(4, 6, MutationRate, PopulationSize)
Hid1ToOut = NEAT(6, 3, MutationRate, PopulationSize)

ObjectType = np.random.choice(['Cactus', 'Bird'], ObjectType.shape)
ObjectLocation = 

for Generation in range(100):
  while np.sum(DinoAlive) != 0:
    # Hi

  HighScore = np.max(np.array(DinoScore + [HighScore]))
  DinoAlive = np.array([True] * PopulationSize, dtype=bool)
  DinoScore = np.array([0] * PopulationSize)
  DinoShape = np.array([60, 40] * PopulationSize)