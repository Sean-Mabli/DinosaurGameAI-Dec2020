import numpy as np

def Sigmoid(In):
  return 1 / (1 + np.exp(-In))

class NEAT:
  def __init__(self, InSize, OutSize, MutationRate, PopulationSize):
    self.Weights = np.random.uniform(-1, 1, (PopulationSize, InSize, OutSize))
    self.Biases = np.random.uniform(0, 0, (PopulationSize, OutSize))
    self.MutationRate, self.PopulationSize = MutationRate, PopulationSize

  def ForwardProp(self, In):
    self.Out = np.inner(In, self.Weights) # + self.Biases
    return self.Out

  def Mutate(self, FavorablePlayer):
    # Copy Weights and Biases
    self.Weights = np.array([self.Weights[FavorablePlayer]] * self.PopulationSize)
    self.Biases = np.array([self.Biases[FavorablePlayer]] * self.PopulationSize)

    # Mutate Weights & Biases
    self.Weights += np.random.uniform(-1, 1, self.Weights.shape) * np.random.choice([0, 1], self.Weights.shape, p=[1 - self.MutationRate, self.MutationRate])
    self.Biases += np.random.uniform(-1, 1, self.Biases.shape) * np.random.choice([0, 1], self.Biases.shape, p=[1 - self.MutationRate, self.MutationRate])