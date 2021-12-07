import numpy as np

def dist(input, x):
    return int(np.sum([x*(x+1)/2 for x in np.abs(input - x)]))

if __name__ == '__main__':
    input = np.loadtxt('input', delimiter=',', dtype=int)

    d = np.inf
    for i in range(np.max(input)):
        c = dist(input, i)
        d = c if c < d else d

    print(d)
