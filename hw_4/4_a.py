n = int(input())
synonyms = dict()
for _ in range(n):
    a, b = input().split()
    synonyms[a] = b
    synonyms[b] = a
query = input()
print(synonyms[query])