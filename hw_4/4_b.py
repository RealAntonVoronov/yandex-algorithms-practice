counter = dict()
with open('input.txt', 'r') as inp:
    for line in inp.readlines():
        for word in line.strip().split():
            print(counter.setdefault(word, 0), end=' ')
            counter[word] += 1