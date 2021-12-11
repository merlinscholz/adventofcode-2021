if __name__ == '__main__':
    input = open('input', 'r').readlines()

    inverse = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    score = lambda x: points[x[0]] if len(x) == 1 else 5*score(x[1:]) + points[x[0]]

    scores = list()

    for line in input:
        stack = list()
        for char in line:
            if char in inverse.keys():
                stack.append(char)
            if char in points.keys():
                if inverse[stack.pop(-1)] != char:
                    stack = list()
                    break

        if len(stack) > 0: scores.append(score([inverse[x] for x in stack]))

    print(sorted(scores)[len(scores)//2])
