import numpy as np
from NN import NN

PopulationSize = 1000

ObjectInfo = np.array((3, 2))
ObjectShape = (80, 40)
DinoShape  = (40, 40)

Gravity = 0.65
Speed = 8
MutationRate = 0.1
Generation = 0

DinoScore = np.array([0] * PopulationSize)
HighScore = 0

DinoAlive = np.array([False] * PopulationSize, dtype=bool)

InToHid1 = np.array([NN(4, 6, 'Identity')] * PopulationSize)
Hid1ToOut = np.array([NN(6, 3, 'Identity')] * PopulationSize)

Players = np.array([NeuralNetwork()] * PopulationSize)
print(Players[0].Score)