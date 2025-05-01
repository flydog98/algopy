# 1141 접두사

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  words = []
  ans = 1

  for _ in range(N):
    words.append(input().strip())

  words.sort()

  for i in range(1, N):
    if not words[i].startswith(words[i - 1]):
      ans += 1

  print(ans)
