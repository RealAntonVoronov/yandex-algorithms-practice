n, k = [int(x) for x in input().split()]
s = input()  # len(s) = n
right = 0
cur_count = {chr(x): 0 for x in range(ord('a'), ord('z')+1)}

max = 0
ans = 0

for left in range(n):
    while right != n and cur_count[s[right]] < k:
        cur_count.setdefault(s[right], 0)
        cur_count[s[right]] += 1
        right += 1
    cur_len = right - left

    if cur_len > max:
        max = cur_len
        ans = left

    cur_count[s[left]] -= 1

print(max, ans+1)