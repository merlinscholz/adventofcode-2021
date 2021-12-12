if __name__ == '__main__':
    input = [x.strip().split('-') for x in open('input', 'r').readlines()]
    conn = {}
    for path in input:
        if path[0] not in conn: conn[path[0]] = list()
        conn[path[0]].append(path[1])
        if path[1] not in conn: conn[path[1]] = list()
        conn[path[1]].append(path[0])

    avail = [['start']]
    counter = 0

    while avail:
        curr = avail.pop()
        for next in conn[curr[-1]]:
            if next == 'end':
                counter += 1
            elif next.isupper() or next not in curr:
                avail.append(curr + [next])

    print(counter)