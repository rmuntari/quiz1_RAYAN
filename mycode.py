import numpy as np
from ROOT import *
Number = 100000
lamda = 0.9
X = 0.1
value_x = [X]

for n in range(Number):
        X = 4*lamda*X*(1 - X)
        value_x.append(X)


value_y = []
for i in value_x:
        value_y.append((2/np.pi)*np.arcsin(np.sqrt(i)))
print value_y

