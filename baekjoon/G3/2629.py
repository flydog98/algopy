# 2629 양팔저울

import sys

input = sys.stdin.readline

if __name__ == "__main__":
  N = 40001
  W = int(input())
  weights = list(map(int, input().split()))
  M = int(input())
  marbles = list(map(int, input().split()))
  answer = []

  dp = [0 for _ in range(N)]

  for weight in weights:
    now = [0 for _ in range(N)]
    for i, tf in enumerate(dp):
      if i == weight:
        now[i] = 1
      if tf == 1:
        if weight + i < N:
          now[weight + i] = 1
        if weight - i > 0:
          now[weight - i] = 1
        if i - weight > 0:
          now[i - weight] = 1
    for i in range(N):
      if now[i] == 1:
        dp[i] = 1

  for marble in marbles:
    if dp[marble] == 1:
      answer.append('Y')
    else:
      answer.append('N')

  print(*answer)
