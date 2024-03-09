# 16225번 제 271회 웰노운컵

import sys
from queue import PriorityQueue

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    q = PriorityQueue()

    comb = []

    for i in range(N):
        comb.append([B[i], A[i]])

    comb.sort()
    ans = comb[0][1]

    for i in range(1, N - 1, 2):
        q.put(-comb[i][1])
        q.put(-comb[i + 1][1])
        num = q.get()
        ans += -num

    print(ans)
