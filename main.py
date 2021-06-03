from phull import Point, convex_hull
from matplotlib import pyplot as plt
import numpy as np

data = [Point(np.random.rand(),np.random.rand()) for i in range(0,50)]
ch = convex_hull(data)
cxs = [A._x for A in ch]
cys = [A._y for A in ch]
xs = [A._x for A in data]
ys = [A._y for A in data]
plt.scatter(xs, ys)
plt.plot(cxs, cys)

plt.show()