n = int(input())
liar = 0
behinders, aheaders = set(), set()
for i in range(n):
    behind, ahead = [int(x) for x in input().split()]
    if behind + ahead != n - 1:
        liar += 1
    else:
        if behind in behinders or ahead in aheaders or behind < 0 or ahead < 0:
            liar += 1
        behinders.add(behind)
        aheaders.add(ahead)
print(n-liar)