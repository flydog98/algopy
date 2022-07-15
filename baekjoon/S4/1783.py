# 1783 병든 나이트

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N, M = map(int, input().split())
  if N == 1:
    print(1)
  elif N == 2:
    print(min(4, int((M + 1) / 2)))
  elif M < 7:
    print(min(4, M))
  else:
    print(M - 2)
