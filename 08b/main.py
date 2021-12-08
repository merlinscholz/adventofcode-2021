from typing import List

import numpy as np

if __name__ == '__main__':
    input1all = [[set(y) for y in x.split('|')[0].split()] for x in open('input', 'r').readlines()]
    input2all = [[set(y) for y in x.split('|')[1].split()] for x in open('input', 'r').readlines()]
    lengthsall = np.vectorize(len)(input1all)

    # TODO Iterate over input lines

    output = [0] * len(input1all)
    for line in range(len(input1all)):
        input1 = np.array(input1all[line])
        input2 = np.array(input2all[line])
        lengths = np.array(lengthsall[line])

        mapping = {}
        a: list[set] = [set] * 10

        a[1] = set(input1[lengths == 2][0])
        a[4] = set(input1[lengths == 4][0])
        a[7] = set(input1[lengths == 3][0])
        a[8] = set(input1[lengths == 7][0])

        mapping[(a[7] - a[1]).pop()] = 'a'

        # Nine
        nine_missing_g = a[4] | a[7]
        for x in a[8] - nine_missing_g:
            if set(x) | nine_missing_g in input1:
                a[9] = set(x) | nine_missing_g
                mapping[x] = 'g'

        # Three
        three_missing_d = a[7] | (a[9] - (a[4] | a[7]))
        for x in a[8] - three_missing_d:
            if set(x) | three_missing_d in input1:
                a[3] = set(x) | three_missing_d
                mapping[x] = 'd'

        # Six
        for x in input1:
            if x | a[1] == a[8] and x != a[8]:
                a[6] = x
                mapping[(a[1] - a[6]).pop()] = 'c'

        mapping[(a[1] & a[6]).pop()] = 'f'

        reverse_mapping = {value : key for (key, value) in mapping.items()}

        # Five
        a[5] = a[9] - set(reverse_mapping['c'])
        a[0] = a[8] - set(reverse_mapping['d'])
        a[2] = a[3] - set(reverse_mapping['f']) | (a[6] - a[5])



        output[line] = int(''.join(str(a.index(x)) for x in input2))

    print(np.sum(output))
    pass