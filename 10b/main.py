if __name__ == '__main__':
    input = open('input', 'r').readlines()

    def inverse(char):
        if char == '(': return ')'
        if char == '[': return ']'
        if char == '{': return '}'
        if char == '<': return '>'

    def points(char):
        if char == ')': return 1
        if char == ']': return 2
        if char == '}': return 3
        if char == '>': return 4

    score = lambda x: points(x[0]) if len(x) == 1 else 5*score(x[1:]) + points(x[0])

    scores = list()

    for line in input:
        stack = list()
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            if char in [')', ']', '}', '>']:
                if inverse(stack.pop(-1)) != char:
                    stack = list()
                    break

        if len(stack) > 0: scores.append(score([inverse(x) for x in stack]))

    print(sorted(scores)[len(scores)//2])
    pass