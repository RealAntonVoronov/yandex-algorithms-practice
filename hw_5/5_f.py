n = int(input())
requirments = [int(a) for a in input().split()]
m = int(input())
minimal_costs = [None for _ in range(1001)]
cur_max_power = 0
for _ in range(m):
    power, cost = [int(x) for x in input().split()]
    if power > cur_max_power:
        cur_max_power = power
    if not minimal_costs[power]:
        minimal_costs[power] = cost
    else:
        minimal_costs[power] = min(cost, minimal_costs[power])
minimal_costs = minimal_costs[:cur_max_power+1]
#print(*minimal_costs)
# reduce:
for i in range(cur_max_power - 1, -1, -1):
    if minimal_costs[i] is None:
        minimal_costs[i] = minimal_costs[i+1]
    else:
        minimal_costs[i] = min(minimal_costs[i], minimal_costs[i+1])
#print(*minimal_costs)
# calculate
res = 0
for i in range(n):
    res += minimal_costs[requirments[i]]
print(res)