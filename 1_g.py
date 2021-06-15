n, k, m = [int(x) for x in input().split()]
# n, k, m = np.random.randint(1, 201, 3)
# print(n, k, m)
rest = n
n_det = 0
while rest >= k:
    #print(rest)
    n_zag = rest // k
    rest = rest % k

    n_det += n_zag * (k // m)
    if k >= m:
        rest += n_zag * (k % m)
print(n_det)
