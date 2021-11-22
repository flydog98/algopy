# 23559번 밥

import sys

if __name__ == '__main__':
  N, X = map(int, sys.stdin.readline().split())

  taste = []
  taste_sum = 0
  money = 0

  for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if(b >= a):
      taste_sum += b
      money += 1000
    else:
      taste.append([a, b])
  
  taste = sorted(taste, key = lambda dif: dif[0] - dif[1])

  for at, today in enumerate(taste):
    remain = len(taste) - at
    max5000 = (X - money) / 5000
    if(remain <= max5000):
      taste_sum += today[0]
      money += 5000
    else:
      taste_sum += today[1]
      money += 1000

  print(taste_sum)
