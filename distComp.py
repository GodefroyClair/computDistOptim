import timeit

import numpy as np
import pandas as pd

from distOptim2 import dist as dist2

# from dist import dist

np.random.seed(42)
size = 1300
compCords = pd.DataFrame(
    {'compLat': np.random.uniform(-30, 30, size),
        'compLong': np.random.uniform(-30, 30, size)})
prospCords = pd.DataFrame(
    {'prospLat': np.random.uniform(-30, 30, size),
        'prospLong': np.random.uniform(-30, 30, size)})


# loop function
# start = timeit.default_timer()
# dfprosp = dist(compCords, prospCords)
# stop = timeit.default_timer()

# apply function
start2 = timeit.default_timer()
dfprosp = dist2(compCords, prospCords)
stop2 = timeit.default_timer()
# print(dfprosp)

# print('Time for normal dist: ', stop - start)
print('Time for optimized dist: ', stop2 - start2)
