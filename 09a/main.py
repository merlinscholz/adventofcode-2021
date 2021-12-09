import numpy as np

if __name__ == '__main__':
    input = np.array([[y for y in x.strip()] for x in open('input').readlines()], dtype=int)


    low = np.full_like(input, False, dtype=bool)
    input = np.pad(input, ((1, 1), (1, 1)), 'constant', constant_values=99999)

    for x in range(1, input.shape[0]-1):
        for y in range(1, input.shape[1] - 1):
            low[x-1,y-1] = input[x, y] < input[x - 1, y] \
                            and input[x, y] < input[x, y - 1] \
                            and input[x, y] < input[x + 1, y] \
                            and input[x, y] < input[x, y + 1]

    tmp = input[1:-1, 1:-1] + 1
    print(np.sum(tmp[low]))
