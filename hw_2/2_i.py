n, m, k = [int(x) for x in input().split()]
field = [[0]*(m + 2) for _ in range(n + 2)]
mines = []
for _ in range(k):
    x, y = [int(coord) for coord in input().split()]
    field[x][y] = '*'
for i in range(n+1):
    for j in range(m+1):
        if field[i][j] != '*':
            cnt = 0
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if field[i + a][j + b] == '*':
                        cnt += 1
            field[i][j] = cnt
for i in range(1, n + 1):
    print(*field[i][1:-1])