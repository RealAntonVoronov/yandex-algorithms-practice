n = int(input())
vocab = {}
for _ in range(n):
    word = input()
    if word.lower() not in vocab:
        vocab[word.lower()] = [word]
    else:
        vocab[word.lower()].append(word)

line = input()
res = 0

for word in line.split():
    udarnyie = [x for x in word if x.isupper()]
    if len(udarnyie) != 1:
        res += 1
    else:
        if (word.lower() in vocab) and (word not in vocab[word.lower()]):
            res += 1
print(res)