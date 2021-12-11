# 1766번 문제집 해결

import sys
import heapq

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    before = [[] for _ in range(N + 1)]
    after = [[] for _ in range(N + 1)]
    solved = [[] for _ in range(N + 1)]
    tracked = [False] * (N + 1)

    for _ in range(M):
        A, B = map(int, input().split())
        before[B].append(A)
        after[A].append(B)

    solvable = []

    for at, i in enumerate(before[1:]):
        if not i:
            heapq.heappush(solvable, at + 1)
            tracked[at + 1] = True

    ans = []
    while solvable:
        temp = heapq.heappop(solvable)
        ans.append(temp)
        for n in after[temp]:
            solved[n].append(temp)
            if len(before[n]) == len(solved[n]) and tracked[n] == False:
                heapq.heappush(solvable, n)
                tracked[n] = True
    print(*ans, sep = ' ')

if __name__ == "__main__":
    main()
