import numpy as np

if __name__ == '__main__':
    input = np.array([[y for y in x.strip()] for x in open('input').readlines()], dtype=int)


    padded = np.pad(input, ((1, 1), (1, 1)), 'constant', constant_values=9)
    basin = np.full_like(padded, -1)
    i = 0

    for x in range(1, padded.shape[0]-1):
        for y in range(1, padded.shape[1] - 1):
            if padded[x, y] < padded[x - 1, y] \
                    and padded[x, y] < padded[x, y - 1] \
                    and padded[x, y] < padded[x + 1, y] \
                    and padded[x, y] < padded[x, y + 1]:
                basin[x, y] = i
                i+=1

    while (padded[basin==-1]!=9).any():
        for x in range(1, padded.shape[0]-1):
            for y in range(1, padded.shape[1]-1):
                if basin[x, y] != -1:
                    if padded[x + 1, y] != 9: basin[x + 1, y] = basin[x, y]
                    if padded[x, y + 1] != 9: basin[x, y + 1] = basin[x, y]
                    if padded[x - 1, y] != 9: basin[x - 1, y] = basin[x, y]
                    if padded[x, y - 1] != 9: basin[x, y - 1] = basin[x, y]

    print(np.prod(np.sort([np.count_nonzero(basin==x) for x in np.sort(np.unique(basin))[1:]])[-3:]))
