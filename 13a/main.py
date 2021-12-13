import numpy as np

if __name__ == '__main__':
    cutoff = -1
    with open('input', 'r') as file:
        for idx, line in enumerate(file):
            if "fold" in line:
                cutoff = idx
                break
        file.seek(0, 0)
        input_folds = [x.strip().split('=') for x in file.readlines()[cutoff:]]
        file.seek(0, 0)
        input_dots = np.loadtxt(file, max_rows=cutoff, delimiter=',', dtype=int)

    working = np.full((np.amax(input_dots[:, 0]) + 1, np.amax(input_dots[:, 1]) + 1), False)
    for dot in input_dots:
        working[dot[0], dot[1]] = True

    fold = input_folds[0]
    line = int(fold[1])
    if fold[0] == 'fold along x':
        left_half = working[:line, :]
        right_half = working[line+1:, :]
        if left_half.shape[0] > right_half.shape[0]:
            right_half = np.pad(right_half, ((0, left_half.shape[0] - right_half.shape[0]), (0, 0)), constant_values=False)
        elif left_half.shape[0] < right_half.shape[0]:
            left_half = np.pad(left_half, ((right_half.shape[0] - left_half.shape[0], 0), (0, 0)), constant_values=False)
        working = np.logical_or(left_half, np.flip(right_half, axis=0))
    elif fold[0] == 'fold along y':
        top_half = working[:, :line]
        bottom_half = working[:, line+1:]
        if top_half.shape[1] > bottom_half.shape[1]:
            bottom_half = np.pad(bottom_half, ((0, 0), (0, top_half.shape[1] - bottom_half.shape[1])), constant_values=False)
        elif top_half.shape[1] < bottom_half.shape[1]:
            top_half = np.pad(top_half, ((0, 0), (bottom_half.shape[1] - top_half.shape[1], 0)), constant_values=False)
        working = np.logical_or(top_half, np.flip(bottom_half, axis=1))
    print(np.count_nonzero(working))


    pass