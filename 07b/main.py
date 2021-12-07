import numpy as np

if __name__ == '__main__':
    input = np.loadtxt('input', delimiter=',', dtype=int)

    c = lambda x: int(np.sum(np.abs(input - x)*(np.abs(input - x)+1)/2))
    d = np.vectorize(c)(np.arange(0, input.size))

    print(np.min(d))
