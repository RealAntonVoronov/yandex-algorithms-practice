n = int(input())
peaks = []
for i in range(n):
    x, y = [int(_) for _ in input().split()]
    peaks.append(y)

left_to_right_increasing_sum = [0] * n
for i in range(1, n):
    left_to_right_increasing_sum[i] = left_to_right_increasing_sum[i-1] + max(0, peaks[i] - peaks[i-1])

right_to_left_increasing_sum = [0] * n
for i in range(n-2, -1, -1):
    right_to_left_increasing_sum[i] = right_to_left_increasing_sum[i+1] + max(0, peaks[i] - peaks[i+1])

"""print(*peaks)
print(*left_to_right_increasing_sum)
print(*right_to_left_increasing_sum)"""
m = int(input())
for i in range(m):
    start, finish = [int(x) - 1 for x in input().split()]
    increasing_sum = left_to_right_increasing_sum if start <= finish else right_to_left_increasing_sum
    print(abs(increasing_sum[finish] - increasing_sum[start]))

