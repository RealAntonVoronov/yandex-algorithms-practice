n = int(input())
mikes = [int(x) for x in input().split()]
m = int(input())
shtans = [int(x) for x in input().split()]

pointer_m, pointer_s = 0, 0
m_value, s_value = mikes[pointer_m], shtans[pointer_s]
min_diff = (mikes[-1] - shtans[0]) + 1
ans = (0, 0)

while pointer_m < len(mikes) and pointer_s < len(shtans):
    m_value, s_value = mikes[pointer_m], shtans[pointer_s]
    diff = abs(m_value - s_value)
    if diff < min_diff:
        min_diff = diff
        ans = (m_value, s_value)
    if m_value > s_value:
        pointer_s += 1
    elif m_value < s_value:
        pointer_m += 1
    else:
        break

print(*ans)