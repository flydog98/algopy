# 10422번 괄호

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  T = int(input())

  parentheses = [0] * 5001
  parentheses[0] = 1
  parentheses[2] = 1

  for i in range(4, 5001, 2):
    temp = 0
    for j in range(2, i + 1, 2):
      temp += parentheses[j - 2] * parentheses[i - j]
      temp %= 1000000007
    parentheses[i] = temp

  for _ in range(T):
    n = int(input())
    print(parentheses[n])
