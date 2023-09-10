# 16496 큰 수 만들기

import sys
from functools import cmp_to_key

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def compare(a, b):
    comp1 = a + b
    comp2 = b + a

    for i, j in zip(comp1, comp2):
        if (i == j):
            continue
        return int(j) - int(i)

    return 0


if __name__ == "__main__":
    N = int(input())
    input = input().strip().split()
    sort = sorted(input, key=cmp_to_key(compare))

    if (sort[0] == '0'):
        print(0)
    else:
        print(''.join(sort))
