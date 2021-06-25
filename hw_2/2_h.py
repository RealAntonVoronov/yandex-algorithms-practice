a = [int(x) for x in input().split()]
max_pos_1, max_pos_2, max_pos_3 = 0, 0, 0
max_neg_1, max_neg_2, max_neg_3 = 0, 0, 0
min_neg_1, min_neg_2 = 0, 0
pos_cnt, neg_cnt = 0, 0
if len(a) < 3:
    print(0)
else:
    for i in range(len(a)):
        if a[i] > 0:
            pos_cnt += 1
            if a[i] > max_pos_1:
                max_pos_1, max_pos_2, max_pos_3 = a[i], max_pos_1, max_pos_2
            elif a[i] > max_pos_2:
                max_pos_2, max_pos_3 = a[i], max_pos_2
            elif a[i] > max_pos_3:
                max_pos_3 = a[i]
        elif a[i] < 0:
            neg_cnt += 1
    zero_cnt = len(a) - pos_cnt - neg_cnt
    if pos_cnt == 0 and zero_cnt > 0:
        if zero_cnt == 3:
            print(0, 0, 0)
        elif zero_cnt == 2:
            for i in range(len(a)):
                if a[i] < 0:
                    print(0, 0, a[i])
                    break
        else:
            for i in range(len(a)):
                if a[i] < min_neg_1:
                    min_neg_1, min_neg_2 = a[i], min_neg_1
                elif a[i] < min_neg_2:
                    min_neg_2 = a[i]
            print(0, min_neg_1, min_neg_2)
    elif pos_cnt == 0:
        # ans < 0
        for i in range(len(a)):
            if a[i] < 0:
                if max_neg_1 == 0:
                    max_neg_1 = a[i]
                elif max_neg_2 == 0:
                    max_neg_2 = a[i]
                elif max_neg_3 == 0:
                    max_neg_3 = a[i]
                elif a[i] > max_neg_1:
                    max_neg_1, max_neg_2, max_neg_3 = a[i], max_neg_1, max_neg_2
                elif a[i] > max_neg_2:
                    max_neg_2, max_neg_3 = a[i], max_neg_2
                elif a[i] > max_neg_3:
                    max_neg_3 = a[i]
        print(max_neg_1, max_neg_2, max_neg_3)
    elif pos_cnt == 1 and neg_cnt >= 2:
        # ans = pos * max(neg * neg)
        for i in range(len(a)):
            if a[i] < min_neg_1:
                min_neg_1, min_neg_2 = a[i], min_neg_1
            elif a[i] < min_neg_2:
                min_neg_2 = a[i]
        print(max_pos_1, min_neg_1, min_neg_2)
    elif pos_cnt == 1 and neg_cnt >= 1:
        # ans = pos * 0 * neg
        for i in range(len(a)):
            if a[i] < 0:
                max_neg_1 = a[i]
        print(0, max_pos_1, max_neg_1)
    elif pos_cnt == 1:
        print(0, 0, max_pos_1)
    elif pos_cnt == 2 and neg_cnt >= 2:
        for i in range(len(a)):
            if a[i] < min_neg_1:
                min_neg_1, min_neg_2 = a[i], min_neg_1
            elif a[i] < min_neg_2:
                min_neg_2 = a[i]
        print(max_pos_1, min_neg_1, min_neg_2)
    elif pos_cnt == 2:
        if zero_cnt > 0:
            print(max_pos_1, max_pos_2, 0)
        else:
            for i in range(len(a)):
                if a[i] < 0:
                    print(max_pos_1, max_pos_2, a[i])
    elif pos_cnt >= 3:
        for i in range(len(a)):
            if a[i] < min_neg_1:
                min_neg_1, min_neg_2 = a[i], min_neg_1
            elif a[i] < min_neg_2:
                min_neg_2 = a[i]
        if max_pos_1 * max_pos_2 * max_pos_3 > max_pos_1 * min_neg_1 * min_neg_2:
            print(max_pos_1, max_pos_2, max_pos_3)
        else:
            print(max_pos_1, min_neg_1, min_neg_2)