# 1744번 수 묶기

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())

  negative = []
  zeros = 0
  ones = 0
  positive = []

  ans = 0


  for _ in range(N):
    number = int(input())
    if(number < 0):
      negative.append(number)
    elif(number > 1):
      positive.append(number)
    elif number == 1:
      ones += 1
    else:
      zeros += 1
  
  negative.sort()
  positive.sort(reverse = True)

  while(len(positive) > 1):
    ans += (positive.pop(0) * positive.pop(0))
  if positive:
    ans += positive[0]

  while(len(negative) > 1):
    ans += (negative.pop(0) * negative.pop(0))
  
  if negative and zeros == 0:
    ans += negative[0]

  ans += ones

  print(ans)
