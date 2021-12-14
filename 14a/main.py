from collections import Counter

if __name__ == '__main__':
    input = [x.strip() for x in open('input').readlines()]
    tuples = {}
    for i in range(len(input[0])-1):
        values = "".join(input[0][i:i+2])
        if values not in tuples.keys(): tuples[values] = 0
        tuples[values] += 1

    # TODO Map to tuple of split values

    rules = {x.split(' -> ')[0]: (x.split(' -> ')[0][0] + x.split(' -> ')[1], x.split(' -> ')[1] + x.split(' -> ')[0][1]) for x in input[2:]}
    counter = Counter(tuples)

    for iteration in range(10):
        next_counter = Counter()
        for item, occur in counter.items():
            next_counter[rules[item][0]] += occur
            next_counter[rules[item][1]] += occur
        counter = next_counter

    count = Counter()
    for item, occur in counter.items():
        count[item[0]] += occur
    mostCommon = count.most_common()
    print(mostCommon[0][1]+1-mostCommon[-1][1])

    pass