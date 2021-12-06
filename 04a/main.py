import numpy as np

if __name__ == '__main__':
    draws = np.loadtxt("input", dtype=int, max_rows=1, delimiter=',')
    fields = np.loadtxt("input", dtype=int, skiprows=2)
    fields = np.array(np.split(fields, len(fields)/5, axis=0))
    fields_mask = np.full(fields.shape, False)

    for draw in draws:
        fields_mask[fields == draw] = True
        for i in range(fields.shape[0]):
            if fields_mask[i].all(axis=0).any() or fields_mask[i].all(axis=1).any():
                print(np.sum(np.ma.masked_array(fields[i], mask=fields_mask[i]))*draw)
                exit()
