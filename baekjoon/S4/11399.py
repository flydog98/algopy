# 11399번 ATM

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  amount = input()

  times = list(map(int, input().split()))

  times.sort()

  ans = 0
  elapsed = 0

  for time in times:
    elapsed += time
    ans += elapsed

  print(ans)
  