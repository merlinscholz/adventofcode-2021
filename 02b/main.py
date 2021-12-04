if __name__ == '__main__':
    input = open('input', 'r').readlines()
    depth = 0
    horizontal = 0
    aim = 0

    for line in input:
        (direction, amount) = line.split(' ')
        if direction == 'forward':
            horizontal += int(amount)
            depth += aim*int(amount)
        elif direction == 'down':
            aim += int(amount)
        elif direction == 'up':
            aim -= int(amount)

    print(depth * horizontal)
