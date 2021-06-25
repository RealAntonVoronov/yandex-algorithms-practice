n = int(input())
scores = [float(x) for x in input().split()]
winners_score = max(scores)
winners_idx = min([i for i in range(n) if scores[i] == winners_score])

if n < 3:
    print(0)
else:
    max_possible_vasiliys = 0

    for i in range(1, len(scores) - 1):
        if scores[i] % 10 == 5 and scores[i + 1] < scores[i] and i > winners_idx:
            if scores[i] > max_possible_vasiliys:
                max_possible_vasiliys = scores[i]
    if not max_possible_vasiliys:
        print(0)
    else:
        ans = 1
        for i in range(len(scores)):
            if scores[i] > max_possible_vasiliys:
                ans += 1
        print(ans)