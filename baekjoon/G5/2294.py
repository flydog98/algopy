# 2294 동전2

import sys

input = sys.stdin.readline

if __name__ == "__main__":
  n, k = map(int, input().split())
  values = []
  dp = [100000000 for _ in range(k + 1)]

  for _ in range(n):
    value = int(input())
    values.append(value)

  for i in range(1, k + 1):
    for value in values:
      if i - value == 0:
        dp[i] = 1
      elif i - value > 0 and dp[i - value] > 0:
        dp[i]  = min(dp[i], dp[i - value] + 1)

  if dp[k] == 100000000:
    print(-1)
  else:
    print(dp[k])
  