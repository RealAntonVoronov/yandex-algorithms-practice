def main():
    n = int(input())

    points = []
    for _ in range(n):
        points.append([int(x) for x in input().split()])

    res = 0

    for i in range(n):
        central_point = points[i]
        seen_points = set()
        distances = []
        for j in range(n):
            dx = central_point[0] - points[j][0]
            dy = central_point[1] - points[j][1]
            distances.append(dx**2 + dy**2)
            if (-dx, -dy) in seen_points:
                res -= 1
            seen_points.add((dx, dy))
        distances.sort()
        distances.append([0, (0, 0)])
        # skip first one because dist to it always zero (dist to itself)
        left = 1
        right = 2

        while right != n+1:
            if distances[left] == distances[right]:
                right += 1
            else:
                res += ((right - left) * (right - left - 1))//2
                left, right = right, right + 1
        # print(i+1, res)
    return res


if __name__ == '__main__':
    res = main()
    print(res)