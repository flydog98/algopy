# 1655번 가운데를 말해요

import sys
import heapq

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  lesser = []
  greater = []

  mid = int(input())
  print(mid)

  for _ in range(N - 1):
    number = int(input())
    if number < mid: # 현재 중앙값보다 작은 수가 들어옴
      if len(lesser) < len(greater): # 작은 쪽 수가 더 적다
        heapq.heappush(lesser, -number)
      else: # 큰 쪽이 적거나 수가 같다
        heapq.heappush(greater, mid)
        heapq.heappush(lesser, -number)
        mid = -heapq.heappop(lesser)
      
    else: # 현재 중앙값 이상의 수가 들어옴
      if len(lesser) < len(greater): # 작은 쪽 수가 더 적다
        heapq.heappush(lesser, -mid)
        heapq.heappush(greater, number)
        mid = heapq.heappop(greater)
      else:
        heapq.heappush(greater, number)

    print(mid)
