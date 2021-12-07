import numpy as np

if __name__ == '__main__':
    input = np.array(np.genfromtxt('input', delimiter=1, dtype=np.uint8), dtype=bool)
    bitsum = np.sum(input, axis=0)

    gamma = np.vectorize(lambda x: 1 if x > (len(input)/2) else 0)(bitsum)
    gamma = gamma.dot(1 << np.arange(gamma.shape[-1] - 1, -1, -1))
    epsilon = 2**len(input[0])-1 ^ gamma

    print(gamma*epsilon)