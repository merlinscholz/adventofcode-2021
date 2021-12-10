if __name__ == '__main__':
    input = open('input', 'r').readlines()

    def inverse(char):
        if char == '(': return ')'
        if char == '[': return ']'
        if char == '{': return '}'
        if char == '<': return '>'

    def points(char):
        if char == ')': return 3
        if char == ']': return 57
        if char == '}': return 1197
        if char == '>': return 25137

    errors = list()

    for line in input:
        stack = list()
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            if char in [')', ']', '}', '>']:
                if inverse(stack.pop(-1)) != char:
                    errors.append(char)

    print(sum([points(x) for x in errors]))