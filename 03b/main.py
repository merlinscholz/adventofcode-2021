if __name__ == '__main__':
    input = [[int(y) for y in x.strip()] for x in open('input', 'r').readlines()]

    # Oxygen
    oxygen = input.copy()
    for i in range(len(oxygen[0])):
        if sum([x[i] for x in oxygen]) >= len(oxygen) / 2:
            oxygen = [x for x in oxygen if x[i] == 1]
        else:
            oxygen = [x for x in oxygen if x[i] == 0]

        if(len(oxygen) == 1):
            oxygen_final = int(''.join(str(x) for x in oxygen[0]), 2)
    co2 = input.copy()
    for i in range(len(co2[0])):
        if sum([x[i] for x in co2]) < len(co2) / 2:
            co2 = [x for x in co2 if x[i] == 1]
        else:
            co2 = [x for x in co2 if x[i] == 0]

        if(len(co2) == 1):
            c02_final = int(''.join(str(x) for x in co2[0]), 2)

    print(oxygen_final * c02_final)