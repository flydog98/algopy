# 1789 수들의 합

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  S = int(input())
  sum = 1
  N = 1

  while True:
    if sum + N + 1 > S:
      break
    N += 1
    sum += N
    
  print(N)
