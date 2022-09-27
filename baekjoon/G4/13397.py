# 13397번 구간 나누기 2

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def isPossible(mid):
  global N, M, numbers
  min_v = 10001
  max_v = -1
  count = 1
  for i in range(N):
    min_v = min(numbers[i], min_v)
    max_v = max(numbers[i], max_v)

    if (mid < max_v - min_v):
      count += 1
      min_v = numbers[i]
      max_v = numbers[i]

  return count <= M

if __name__ == "__main__":
  global N, M, numbers

  N, M = map(int, input().split())
  numbers = list(map(int, input().split()))

  left = -1
  right = 10001

  while(left <= right):
    mid = int((left + right) / 2)
    if isPossible(mid):
      right = mid - 1
    else:
      left = mid + 1

  print(left)
