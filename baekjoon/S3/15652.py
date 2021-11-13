# 15652번 N과 M (4)

import sys
from itertools import combinations_with_replacement

if __name__ == '__main__':
  N, M = map(int, sys.stdin.readline().split())
  numbers = [n + 1 for n in range(N)]

  for cwr in combinations_with_replacement(numbers, M):
    print(*cwr)
