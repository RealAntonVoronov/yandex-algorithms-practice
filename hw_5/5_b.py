n, k = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
res = 0
prefix_sums = [0] * (n + 1)

for i in range(n):
    prefix_sums[i+1] = numbers[i] + prefix_sums[i]

print(*numbers)
print(*prefix_sums)

left = 0
right = 1

while right < n + 1:
    lr_sum = prefix_sums[right] - prefix_sums[left]
    if lr_sum == k:
        res += 1
        left += 1
        right += 1
    elif lr_sum > k:
        left += 1
    else:
        right += 1
print(res)