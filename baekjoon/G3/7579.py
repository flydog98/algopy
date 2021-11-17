# 7579번 앱

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N, M = map(int, input().split())

  A = list(map(int, input().split()))
  c = list(map(int, input().split()))

  dp = [[0 for _ in range(sum(c) + 1)] for _ in range(N + 1)]

  for i, (memory, cost) in enumerate(zip(A, c), 1):
    for max_cost in range(sum(c) + 1): #(N*100 + 1):
      nowmax = dp[i - 1][max_cost - cost] + memory if max_cost - cost >= 0 else 0
      dp[i][max_cost] = max(nowmax, dp[i - 1][max_cost])

  for i, candidate in enumerate(dp[N]):
    if(candidate >= M):
      print(i)
      break
  