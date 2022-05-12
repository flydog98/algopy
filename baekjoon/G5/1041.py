# 1041번 주사위

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  A, B, C, D, E, F = list(map(int, input().split()))
  numbers = [A, B, C, D, E, F]

  min3 = min([A+B+C, A+B+D, A+C+E, A+D+E, B+C+F, B+D+F, C+E+F, D+E+F])
  min2 = min([A+B,A+C,A+D,A+E,B+C,B+D,B+F,C+E,C+F,D+E,D+F,E+F])
  min1 = min(numbers)
  
  if(N == 1):
    numbers.remove(max(numbers))
    print(sum(numbers))
  else:
    print(min3 * 4 + min2 * (8 * N - 12) + min1 * (5 * N * N - 16 * N + 12))