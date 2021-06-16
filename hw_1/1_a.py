temps = list(map(int, input().split()))
t_room, t_cond = temps[0], temps[1]
mode = input()

if mode == 'fan':
	t_res = t_room
elif mode == 'auto':
	t_res = t_cond
elif mode == 'heat' and t_room < t_cond:
	t_res = t_cond
elif mode == 'heat':
	t_res = t_room
elif mode == 'freeze' and t_room > t_cond:
	t_res = t_cond
elif mode == 'freeze':
	t_res = t_room
else:
	t_res = None
print(t_res)
