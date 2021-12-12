if __name__ == '__main__':
    input = [x.strip().split('-') for x in open('input', 'r').readlines()]
    map = {}
    for path in input:
        if path[0] not in map: map[path[0]] = list()
        map[path[0]].append(path[1])
        if path[1] not in map: map[path[1]] = list()
        map[path[1]].append(path[0])

    paths_to_finish = [['start']]
    counter = 0

    while paths_to_finish:
        current_path = paths_to_finish.pop()
        if current_path[-1] == 'end':
            counter += 1
            continue
        for next_cave in map[current_path[-1]]:
            if next_cave.islower() and next_cave in current_path:
                continue
            paths_to_finish.append(current_path + [next_cave])

    print(counter)