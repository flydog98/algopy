# 2805번 나무 자르기

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


if __name__ == "__main__":

    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    top = max(trees)
    bot = 0
    answer = 0

    while (bot <= top):
        mid = (top + bot) // 2
        amount = 0

        for i in range(N):
            if (trees[i] > mid):
                amount += trees[i] - mid

        if (amount >= M):
            answer = mid
            bot = mid + 1
        else:
            top = mid - 1

    print(answer)
