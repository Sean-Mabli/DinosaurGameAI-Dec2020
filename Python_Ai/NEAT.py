import numpy as np

def Sigmoid(In):
  return 1 / (1 + np.exp(-In))

class NEAT:
  def __init__(self, InSize, OutSize, MutationRate, PopulationSize):
    self.Weights = np.random.uniform(-1, 1, (PopulationSize, InSize, OutSize))
    self.Biases = np.random.uniform(0, 0, (PopulationSize, OutSize))
    self.MutationRate, self.PopulationSize = MutationRate, PopulationSize

  def ForwardProp(self, In):
    self.Out = np.multiply(In, np.transpose(self.Weights, axes=(2, 0, 1)))
    self.Out = np.transpose(np.sum(self.Out, axis=2), axes=(1, 0)) + self.Biases
    return Sigmoid(self.Out)

  def Mutate(self, FavorablePlayer):
    # Copy Weights and Biases
    self.Weights = np.array([self.Weights[FavorablePlayer]] * self.PopulationSize)
    self.Biases = np.array([self.Biases[FavorablePlayer]] * self.PopulationSize)

    # Mutate Weights & Biases
    self.Weights *= np.random.choice([0, 1], self.Weights.shape, p=[self.MutationRate, 1 - self.MutationRate])
    self.Weights = np.where(self.Weights == 0, np.random.uniform(-1, 1, self.Weights.shape), self.Weights)

    self.Biases *= np.random.choice([0, 1], self.Biases.shape, p=[self.MutationRate, 1 - self.MutationRate])
    self.Biases = np.where(self.Biases == 0, np.random.uniform(-1, 1, self.Biases.shape), self.Biases)