import numpy as np

if __name__ == '__main__':
    input = np.loadtxt('input', delimiter=',', dtype=int)

    c = lambda x: np.sum(np.abs(input - x))
    d = np.vectorize(c)(np.arange(0, input.size))

    print(np.min(d))
