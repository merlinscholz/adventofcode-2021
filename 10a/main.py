if __name__ == '__main__':
    input = open('input', 'r').readlines()

    inverse = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    errors = list()

    for line in input:
        stack = list()
        for char in line:
            if char in inverse.keys():
                stack.append(char)
            if char in points.keys():
                if inverse[stack.pop(-1)] != char:
                    errors.append(char)
                    break

    print(sum([points[x] for x in errors]))