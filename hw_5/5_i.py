def main():
    k = int(input())
    string = input()
    res = 0
    n = len(string)
    if n == 1:
        return res
    else:
        prevlen = 0
        for left in range(k, n):
            if string[left] == string[left - k]:
                prevlen += 1
                res += prevlen
            else:
                prevlen = 0

        return res


if __name__ == '__main__':
    res = main()
    print(res)

