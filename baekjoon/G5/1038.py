# 1038 감소하는 수

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())

  dp = [[[] for _ in range(10)] for _ in range(11)]

  for i in range(10):
    dp[1][i].append(i)

  for i in range(2, 11):
    for j in range(1, 10):
      for k in range(j):
        for before in dp[i- 1][k]:
          dp[i][j].append(before + j * 10**(i - 1))

  flattened = [x for i in range(1, 11) for j in range(10) for x in dp[i][j]]

  if N >= len(flattened):
    print(-1)
  else:
    print(flattened[N])
