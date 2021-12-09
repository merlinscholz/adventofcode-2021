from typing import List

import numpy as np

if __name__ == '__main__':
    input = np.array([[set(y) for y in x.split()[:]] for x in open('input', 'r').readlines()])


    def calc(input):
        lengths = list(np.vectorize(len)(input))

        a: list[set] = [None] * 11 # a[10] is the minus sign, needed to convert 8 to 0
        a[1] = set(input[lengths.index(2)])
        a[4] = set(input[lengths.index(4)])
        a[7] = set(input[lengths.index(3)])
        a[8] = set(input[lengths.index(7)])

        # Nine
        nine_missing_g = a[4] | a[7]
        for x in a[8] - nine_missing_g:
            if set(x) | nine_missing_g in input:
                a[9] = set(x) | nine_missing_g

        # Three
        three_missing_d = a[7] | (a[9] - (a[4] | a[7]))
        for x in a[8] - three_missing_d:
            if set(x) | three_missing_d in input:
                a[3] = set(x) | three_missing_d
                a[10] = set(x)

        # Six
        for x in input:
            if x | a[1] == a[8] and x != a[8]:
                a[6] = x

        # Five
        a[5] = a[9] - (a[1] - a[6])

        # Zero
        a[0] = a[8] - a[10]

        # Two
        a[2] = a[3] - (a[1] & a[6]) | (a[6] - a[5])

        return np.sum([a.index(x)*y for x, y in zip(input[-4:], [10**exp for exp in np.arange(3, -1, -1)])])


    output = [calc(x) for x in input]
    print(np.sum(output))
