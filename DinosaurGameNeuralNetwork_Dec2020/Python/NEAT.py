import numpy as np
from ActivationFunctions import ForwardProp, BackProp

class NN:
  def __init__(self, InputSize, OutSize, Activation, MutationRate, WeightsInit=(-1, 1), BiasesInit=(0, 0)):
    self.Weights = np.random.uniform(WeightsInit[0], WeightsInit[1], (InputSize, OutSize))
    self.Biases = np.random.uniform(BiasesInit[0], BiasesInit[1], (OutSize))
    self.Activation, self.LearningRate = Activation, LearningRate
    
  def ForwardProp(self, InputLayer):
    self.InputLayer = InputLayer
    self.Out = np.transpose(self.Weights) @ InputLayer + self.Biases
  
    # Apply Activation Function
    self.Out = ForwardProp(self.Out, self.Activation)
    
    return self.Out

  def Mutate(se3lf, FavorableWeights, FavorableBiases):
    self.Weights = FavorableWeights
    self.Biases = FavorableBiases

