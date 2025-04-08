# 2293 동전1

import sys

input = sys.stdin.readline

if __name__ == "__main__":
  n, k = map(int, input().split())
  values = []
  dp = [0 for _ in range(k + 1)]

  for _ in range(n):
    value = int(input())
    values.append(value)

  for value in values:
    for i in range(1, k + 1):
      if i - value == 0:
        dp[i] += 1
      elif i - value > 0:
        dp[i] += dp[i - value]

  print(dp[k])
  