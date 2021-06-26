g_1 = input()
g_2 = input()
cnt = 0
pairs_2 = set()
for i in range(len(g_2) - 1):
    pairs_2.add(g_2[i:i+2])
for i in range(len(g_1) - 1):
    if g_1[i:i+2] in pairs_2:
        cnt += 1
print(cnt)
