# 15989 1, 2, 3 더하기 4

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  T = int(input())

  numbers = [1 for _ in range(10001)]

  for number in range(2, 10001):
    numbers[number] += numbers[number - 2]

  for number in range(3, 10001):
    numbers[number] += numbers[number - 3]

  for _ in range(T):
    n = int(input())
    print(numbers[n])
