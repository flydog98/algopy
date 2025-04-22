# 16895 님 게임 3

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  rocks = list(map(int, input().split()))

  xor = 0
  for rock in rocks:
    xor ^= rock

  if len(rocks) == 1:
    print(1)
  elif xor == 0:
    print(0)
  else:
    ans = 0
    for rock in rocks:
      if xor^rock <= rock:
        ans += 1

    print(ans)
