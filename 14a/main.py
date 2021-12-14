from collections import Counter

if __name__ == '__main__':
    input = [x.strip() for x in open('test').readlines()]
    tuples = {}
    for i in range(len(input[0])-1):
        values = "".join(input[0][i:i+2])
        if values not in tuples.keys(): tuples[values] = 0
        tuples[values] += 1

    # TODO Map to tuple of split values

    rules = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in input[2:]}

    for iteration in range(1):
        iter = tuples.copy()
        for tuple in iter.keys():
            if tuple in rules.keys():
                tuples[tuple] -= iter[tuple]
                if tuple[0] + rules[tuple] not in tuples.keys(): tuples[tuple[0] + rules[tuple]] = 0
                tuples[tuple[0] + rules[tuple]] += iter[tuple]
                if rules[tuple] + tuple[1] not in tuples.keys(): tuples[rules[tuple] + tuple[1]] = 0
                tuples[rules[tuple] + tuple[1]] += iter[tuple]

    print(tuples)
