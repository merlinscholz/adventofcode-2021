import numpy as np

MAX_DAYS_TO_FERTILITY = 8
DAYS_TO_FERTILITY = 6


if __name__ == '__main__':
    input = np.loadtxt('input', delimiter=',', dtype=int)
    unique, counts = np.unique(input, return_counts=True)
    hist = np.zeros(MAX_DAYS_TO_FERTILITY+2, dtype=int)
    hist[unique] = counts

    for day in range(80):
        hist[MAX_DAYS_TO_FERTILITY+1] += hist[0]
        hist[DAYS_TO_FERTILITY+1] += hist[0]
        hist = np.pad(hist, (0, 1), 'constant')[1:]

    print(sum(hist))