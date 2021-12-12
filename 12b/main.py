if __name__ == '__main__':
    input = [x.strip().split('-') for x in open('input', 'r').readlines()]
    map = {}
    for path in input:
        if path[0] not in map: map[path[0]] = list()
        map[path[0]].append(path[1])
        if path[1] not in map: map[path[1]] = list()
        map[path[1]].append(path[0])

    paths_to_finish = [(['start'], False)]
    counter = 0
    all_paths = []

    while paths_to_finish:
        current_path, already_revisited = paths_to_finish.pop(-1)
        if current_path[-1] == 'end':
            counter += 1
            all_paths.append(current_path)
            continue

        for next_cave in map[current_path[-1]]:
            currently_revisiting = already_revisited
            if next_cave == 'start':
                continue
            elif next_cave.islower() and next_cave in current_path and already_revisited:
                continue
            elif next_cave.islower() and next_cave in current_path and not already_revisited:
                currently_revisiting = True
            paths_to_finish.append((current_path + [next_cave], currently_revisiting))

    print(counter)