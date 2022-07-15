# 11047번 동전 0

import sys
from bisect import bisect, bisect_left

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N, K = map(int, input().split())
  coins = []
  for _ in range(N):
    coins.append(int(input()))

  answer = 0
  index = N - 1
  while K != 0 and index >= 0:
    if coins[index] <= K:
      answer += int(K / coins[index])
      K = K % coins[index]
      index -= 1
    else:
      index -= 1

  print(answer)
