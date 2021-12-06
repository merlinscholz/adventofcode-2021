if __name__ == '__main__':
    input = [[int(y) for y in x.strip()] for x in open('input', 'r').readlines()]
    bitsum = [sum(x) for x in zip(*input)]

    gamma = [1 if x > (len(input)/2) else 0 for x in bitsum]
    gamma = int(''.join(str(x) for x in gamma), 2)
    epsilon = 2**len(input[0])-1 ^ gamma

    print(gamma*epsilon)