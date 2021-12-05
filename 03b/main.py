if __name__ == '__main__':
    input = [[int(y) for y in x.strip()] for x in open('input', 'r').readlines()]
    oxygen = input.copy()
    co2 = input.copy()

    for i in range(len(input[0])):
        if(len(oxygen) > 1):
            oxygen = [x for x in oxygen if x[i] == int(sum([x[i] for x in oxygen]) >= len(oxygen) / 2)]
        if(len(co2) > 1):
            co2 =    [x for x in co2    if x[i] == int(sum([x[i] for x in co2   ]) <  len(co2)    / 2)]
        if (len(oxygen) == 1 and len(co2) == 1):
            break

    print(int(''.join(str(x) for x in oxygen[0]), 2) *
          int(''.join(str(x) for x in    co2[0]), 2))