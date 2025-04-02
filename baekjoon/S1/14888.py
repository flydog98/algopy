# 14888번 연산자 끼워넣기

import sys
from itertools import permutations

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  numbers = list(map(int, input().split()))
  oper_num = list(map(int, input().split()))
  oper = []
  min_val = 1000000001
  max_val = -1000000001
  
  for i in range(4):
    for j in range(oper_num[i]):
      oper.append(i)

  for order in permutations(oper, len(oper)):
    value = numbers[0]
    for i in range(N - 1):
      if order[i] == 0:
        value += numbers[i + 1]
      elif order[i] == 1:
        value -= numbers[i + 1]
      elif order[i] == 2:
        value *= numbers[i + 1]
      elif order[i] == 3:
        if value < 0:
          value = - ((- value) // numbers[i + 1])
        else:
          value = value // numbers[i + 1]
    
    min_val = min(min_val, value)
    max_val = max(max_val, value)
  
  print(max_val)
  print(min_val)

    
