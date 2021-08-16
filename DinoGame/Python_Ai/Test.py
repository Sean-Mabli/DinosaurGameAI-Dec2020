import numpy as np
from NEAT import NEAT

InToOut = NEAT(4, 6, MutationRate=0.1, PopulationSize=1000)

In = np.array([0.3, 0.9, 0.1, 0.7])
In = np.array([In] * 1000)

Out = InToOut.ForwardProp(In)
print(In.shape)
print(Out.shape)