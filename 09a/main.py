import numpy as np

if __name__ == '__main__':
    input = np.array([[y for y in x.strip()] for x in open('input').readlines()], dtype=int)


    low = np.full_like(input, False, dtype=bool)
    padded = np.pad(input, ((1, 1), (1, 1)), 'constant', constant_values=9)

    for x in range(1, padded.shape[0]-1):
        for y in range(1, padded.shape[1] - 1):
            low[x-1,y-1] = padded[x, y] < padded[x - 1, y] \
                            and padded[x, y] < padded[x, y - 1] \
                            and padded[x, y] < padded[x + 1, y] \
                            and padded[x, y] < padded[x, y + 1]

    print(np.sum(input[low]+1))
