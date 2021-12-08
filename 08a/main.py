import numpy as np

if __name__ == '__main__':
    input = np.array([x.split('|')[1].split() for x in open('input', 'r').readlines()])

    lengths = np.vectorize(len)(input).flatten()
    print(np.count_nonzero(np.isin(lengths, [2,4,3,7])))
