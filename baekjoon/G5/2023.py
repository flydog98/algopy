# 2023 신기한 소수

import sys
import math

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def check_prime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
    
  return True

if __name__ == "__main__":
  N = int(input())

  pri = [1, 3, 5, 7, 9]
  dp = [2, 3, 5, 7]

  for n in range(2, N + 1):
    next_dp = []

    for d in dp:
      for p in pri:
        now = d * 10 + p
        if check_prime(now) == True:
          next_dp.append(now)

    dp = next_dp

  for d in dp:
    print(d)
