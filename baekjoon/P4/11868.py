# 11868번 님 게임 2

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
    print("koosaga")
  elif xor == 0:
    print("cubelover")
  else:
    ans = 0
    for rock in rocks:
      if xor^rock <= rock:
        ans += 1

    if ans == 0:
      print("cubelover")
    else:
      print("koosaga")
