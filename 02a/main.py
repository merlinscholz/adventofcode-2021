if __name__ == '__main__':
    input = open('input', 'r').readlines()
    depth = 0
    horizontal = 0

    for line in input:
        (direction, amount) = line.split(' ')
        if direction == 'forward':
            horizontal += int(amount)
        elif direction == 'down':
            depth += int(amount)
        elif direction == 'up':
            depth -= int(amount)

    print(depth * horizontal)
