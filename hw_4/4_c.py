counter = {}
cur_max = 0
cur_word_max = ''

with open('input.txt', 'r') as inp:
    for line in inp.readlines():
        for word in line.strip().split():
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
            if counter[word] > cur_max:
                cur_max = counter[word]
                cur_word_max = word
            elif counter[word] == cur_max and word < cur_word_max:
                cur_word_max = word
print(cur_word_max)