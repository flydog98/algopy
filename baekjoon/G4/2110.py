# 2110번 공유기 설치

import sys
from bisect import bisect_left

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def isPossible(mid):
  global N, C, house
  count = 1
  installed = house[0]
  at = bisect_left(house, installed + mid)
  while(installed <= house[-1] and at < N):
    installed = house[at]
    count += 1
    at = bisect_left(house, installed + mid)
  
  return C <= count


if __name__ == "__main__":
  global N, C, house
  N, C = map(int ,input().split())
  house = []

  for _ in range(N):
    house.append(int(input()))

  house.sort()

  left = 1
  right = 1000000000
  while(left <= right):
    mid = (right + left) // 2
    if isPossible(mid):
      left = mid + 1
    else:
      right = mid - 1

  print(right)
