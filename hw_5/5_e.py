def generate(n, k):
    import numpy as np
    result = list(range(1, k+1))
    for i in range(k, n):
        result.append(np.random.randint(1, k+1))
    return np.random.permutation(result)


def find_shortest(colors, k):
    left = 0
    right = 1
    counter = {i: 0 for i in range(1, k+1)}

    n = len(colors)
    cur_best = n

    seen_colors = {colors[left]}
    counter[colors[left]] = 1

    while right != n:
        counter[colors[right]] += 1

        if colors[right] == colors[left]:
            for j in range(left, right):
                if counter[colors[j]] > 1:
                    left += 1
                    counter[colors[j]] -= 1
                else:
                    break
        else:
            seen_colors.add(colors[right])

        if len(seen_colors) == k:
            if right - left <= cur_best:
                cur_best = right - left
                ans = left + 1, right + 1

        right += 1

    return ans


def main():
    n, k = [int(x) for x in input().split()]

    if n == 1:
        return 0, 0

    #colors = generate(n, k)
    #print(colors)
    colors = [int(x) for x in input().split()]

    print(*find_shortest(colors, k))


if __name__ == '__main__':
    main()
