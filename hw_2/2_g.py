a = [int(x) for x in input().split()]
max_pos_1, max_pos_2, max_neg_1, max_neg_2 = 0, 0, 0, 0
count_pos, count_neg = 0, 0
for i in range(len(a)):
    if a[i] > 0 and a[i] > max_pos_1:
        max_pos_1, max_pos_2 = a[i], max_pos_1
        count_pos += 1
    elif a[i] > 0 and a[i] >= max_pos_2:
        max_pos_2 = a[i]
        count_pos += 1
    elif a[i] < 0 and abs(a[i]) > abs(max_neg_1):
        max_neg_1, max_neg_2 = a[i], max_neg_1
        count_neg += 1
    elif a[i] < 0 and abs(a[i]) >= abs(max_neg_2):
        max_neg_2 = a[i]
        count_neg += 1

if count_pos >= 2 or count_neg >= 2:
    if max_pos_1 * max_pos_2 > max_neg_1 * max_neg_2:
        print(max_pos_2, max_pos_1)
    else:
        print(max_neg_1, max_neg_2)
elif count_pos == 1 and count_neg == 1:
    print(max_neg_1, max_pos_1)
elif count_pos == 1 and count_neg > 1:
    print(max_neg_2, max_neg_1)
elif count_pos == 1:
    print(max_pos_2, max_pos_1)
elif count_neg == 1 and count_pos > 1:
    print(max_pos_2, max_pos_1)
else:
    print(max_neg_1, max_neg_2)