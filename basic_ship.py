import numpy as np

from_x = 0
to_x = 1
precision = 0.25
n_x = ( to_x - from_x ) / precision + 1
for i in np.linspace(0, 1, n_x):
    print(i)