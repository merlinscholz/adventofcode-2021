from collections import Counter

if __name__ == '__main__':
    input = [x.strip() for x in open('input').readlines()]
    working = [x for x in input[0]]
    rules = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in input[2:]}

    for iteration in range(10):
        append = list()
        delta = 0
        for i in range(len(working)-1):
            if "".join(working[i+delta:i+delta+2]) in rules.keys():
                working.insert(i + delta+1, rules["".join(working[i+delta:i+delta+2])])
                delta += 1

    counter = Counter(working)
    print(counter.most_common()[0][1] - counter.most_common()[-1][1])
