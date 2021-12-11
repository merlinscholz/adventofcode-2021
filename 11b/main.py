import itertools
import numpy as np

def flash(input, x, y):
    for coord in itertools.product(range(-1, 2), range(-1, 2)):
        if x+coord[0] in range(0, input.shape[0]) and y+coord[1] in range(0, input.shape[1]):
            input[x+coord[0], y+coord[1]] += 1
            if input[x+coord[0], y+coord[1]] == 10:
                input = flash(input, x+coord[0], y+coord[1])

    return input

if __name__ == '__main__':
    input = np.array([[y for y in x.strip()] for x in open('input').readlines()], dtype=int)
    flashes = 0
    step = 0

    while True:
        input += 1
        step += 1

        for coords in np.argwhere(input == 10):
            input = flash(input, *coords)

        flashes += np.count_nonzero(input[input>9])
        input[input>9] = 0
        if np.count_nonzero(input==0) == input.shape[0]*input.shape[1]:
            print(step)
            break