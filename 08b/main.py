if __name__ == '__main__':
    input = [[set(y) for y in x.split()] for x in open('input', 'r').readlines()]

    def calc(input):
        lengths = list(map(len, input))

        a: list[set] = [set()] * 11 # a[10] is the minus sign, needed to convert 8 to 0
        a[1] = set(input[lengths.index(2)])
        a[4] = set(input[lengths.index(4)])
        a[7] = set(input[lengths.index(3)])
        a[8] = set(input[lengths.index(7)])

        nine_missing_g = a[4] | a[7]
        for x in a[8] - nine_missing_g:
            if set(x) | nine_missing_g in input:
                a[9] = set(x) | nine_missing_g

        three_missing_d = a[7] | (a[9] - (a[4] | a[7]))
        for x in a[8] - three_missing_d:
            if set(x) | three_missing_d in input:
                a[3] = set(x) | three_missing_d
                a[10] = set(x)

        for x in input:
            if x | a[1] == a[8] and x != a[8]:
                a[6] = x

        a[5] = a[9] - (a[1] - a[6])
        a[0] = a[8] - a[10]
        a[2] = a[3] - (a[1] & a[6]) | (a[6] - a[5])

        return sum([a.index(x)*y for x, y in zip(input[-4:], [10**exp for exp in range(3, -1, -1)])])

    print(sum(list(map(calc, input))))
