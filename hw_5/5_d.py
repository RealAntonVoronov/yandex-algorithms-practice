n, r = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]  # len(nums) = n
left = n - 2
right = n - 1
res = 0
while left != -1 and right != 0:
    diff = nums[right] - nums[left]
    if diff > r:
        res += left + 1
        right -= 1
    else:
        left -= 1
print(res)