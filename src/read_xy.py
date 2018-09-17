import numpy as np
import pylab as pl

with open("../data/xy.dat", "r") as infile:
    x = []
    y = []
    for line in infile:
        x_, y_ = np.array(line.split(), dtype=float)
        x.append(x_)
        y.append(y_)
    
x = np.array(x)
y = np.array(y)


pl.plot(x, y)
pl.show()
