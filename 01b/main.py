if __name__ == '__main__':
    input = [int(num) for num in open('input', 'r').readlines()]
    counter = 0

    for i in range(3, len(input)):
        if input[i] > input[i-3]:
            counter += 1

    print(counter)
