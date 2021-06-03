from phull import Point
from matplotlib import pyplot as plt
import numpy as np

def get_random_hull_length(n: int) -> float:
    data = [Point(*np.random.multivariate_normal([0,0],[[1,0],[0,1]])) for i in range(0,n)]
    return Point.convex_hull_length(data)


def experiment(lower_n: int, upper_n: int, step_sz: int, am_exps: int):
    #Generated for each n between lower_n and upper_n (with step size step_sz) am_exps many datasets of n normal-distributed points.
    #Then, calculates and plots for each such n the average length of the boundary of the convex hull of the datasets.
    ns = range(lower_n,upper_n, step_sz)
    avg_lengths = []
    for n in ns:
        sum = 0
        for i in range(0,am_exps):
            sum += get_random_hull_length(n)
        #Value to actually calculate. In this case, average length of convex hull boundary
        val = sum/am_exps

        avg_lengths.append(val)
        print(n, val)
    plt.plot(ns, avg_lengths)
    plt.show()

if __name__ == "__main__":
    data = [Point(*np.random.multivariate_normal([0,0],[[1,0],[0,1]])) for i in range(0,100)]
    ch = Point.convex_hull(data)
    
    plt.scatter([P._x for P in data],[P._y for P in data])
    plt.plot([P._x for P in ch],[P._y for P in ch])
    plt.show()

    experiment(5,1000, 5, 10)