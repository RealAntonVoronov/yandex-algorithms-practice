from itertools import permutations


def cubic(cards, m):
    res = set()
    n = len(cards)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if cards[k] / cards[i] <= m:
                    triplet = cards[i], cards[j], cards[k]
                    res.update(permutations(triplet))
    return res


def count_triplets(left, right):
    # segment = (1, 2, 99) right = 3 left = 0
    ans = 0


    return ans


n, k = [int(x) for x in input().split()]
cards = [int(x) for x in input().split()]

counter = {}
for x in cards:
    counter.setdefault(x, 0)
    counter[x] += 1

sorted_keys = sorted(counter.keys())
# print(*sorted_keys)
# print(*[counter[x] for x in sorted_keys])
m = len(sorted_keys)
left = 0
right = 0
ans = 0
duplicates = 0
for left in range(m):
    while right != m and sorted_keys[right] / sorted_keys[left] <= k:
        if counter[sorted_keys[right]] >= 2:
            duplicates += 1
        right += 1

    range_len = right - left - 1
    if counter[sorted_keys[left]] >= 3:  # (1,1,1)
        ans += 1
    if counter[sorted_keys[left]] >= 2:
        ans += 3 * range_len  # (1,1,2), (1,1,3), ... , (1,1,cards[right-1]) and permutations
    # (1,2,2), (1,3,3), ..., (1,cards[right-1], cards[right-1]) and permutations
    if counter[sorted_keys[left]] >= 2:
        duplicates -= 1
    ans += duplicates * 3
    # select two numbers from cards[left+1:right]
    # (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)
    if range_len > 0:
        ans += 3 * (range_len - 1) * range_len

print(ans)

#print(len(cubic(cards, k)), cubic(cards, k))
