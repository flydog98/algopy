# 1541번 잃어버린 괄호

import sys
import re

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  raw = input()
  sum = 0
  minus = 0

  numbers = list(map(int, re.split('[+-]', raw)))
  operators = re.findall('[+-]', raw)

  # print(numbers)
  # print(operators)

  sum = numbers[0]
  for i, cur_operator in enumerate(operators):
    cur_number = numbers[i + 1]
    if cur_operator == '-':
      if minus != 0:
        sum -= minus
        minus = cur_number
      else:
        minus += cur_number
    elif cur_operator == '+':
      if minus != 0:
        minus += cur_number
      else:
        sum += cur_number
  sum -= minus
  print(sum)
