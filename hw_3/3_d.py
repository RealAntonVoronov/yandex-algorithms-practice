import sys
res = 0
vocab = set()
for line in sys.stdin:
    for w in line.strip().split():
        if w not in dict:
            res += 1
            vocab.add(w)
print(res)