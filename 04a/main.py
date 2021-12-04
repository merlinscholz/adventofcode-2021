import numpy as np

if __name__ == '__main__':
    input = open('input', 'r').readlines()
    draws = [int(x) for x in input[0].split(",")]
    fields_raw = "".join(input[2:]).split("\n\n")
    fields = np.array([[[int(y.strip()) for y in x.split()] for x in field.strip("\n").split("\n")] for field in fields_raw])
    fields_mask = np.full(fields.shape, False)

    for draw in draws:
        fields_mask[fields == draw] = True
        for i in range(fields.shape[0]):
            if fields_mask[i].all(axis=0).any() or fields_mask[i].all(axis=1).any():
                tmp = np.ma.masked_array(fields[i], mask=fields_mask[i])
                print(np.sum(tmp)*draw)
                exit()
