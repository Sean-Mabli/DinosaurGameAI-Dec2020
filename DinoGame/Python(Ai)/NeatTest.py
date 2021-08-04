import numpy as np
from NEAT import NEAT

InToHid1 = NEAT(4, 6, MutationRate=0.1, PopulationSize=1000)
Hid1ToOut = NEAT(6, 3, MutationRate=0.1, PopulationSize=1000)

In = np.zeros((1000, 4))
# print(In.shape)
Weights = np.zeros((1000, 4, 6))
print((np.transpose(Weights[0, :, :]) @ In[0, :]).shape)

# Hid1 = InToHid1.ForwardProp(In)
# Out = Hid1ToOut.ForwardProp(Hid1)
# print(Hid1.shape)