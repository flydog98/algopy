# 1422 숫자의 신

import sys
from functools import cmp_to_key

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def compare(a, b):  # 전체 정렬 용도
    comp1 = a + b
    comp2 = b + a

    for i, j in zip(comp1, comp2):
        if (i == j):
            continue
        return int(j) - int(i)

    return 0


def compare2(a, b):  # 가장 좋은 수 찾기 용도
    if (len(a) == len(b)):
        return compare(a, b)
    return len(b) - len(a)


if __name__ == "__main__":
    N, K = map(int, input().split())

    line = []

    for i in range(N):
        line.append(input().strip())

    sort = sorted(line, key=cmp_to_key(compare))
    most = sorted(line, key=cmp_to_key(compare2))[0]
    printed = False

    for num in sort:
        print(num, end='')
        if (num == most and not printed):
            for i in range(K - N):
                print(num, end='')
            printed = True
    print()
