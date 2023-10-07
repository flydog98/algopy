# 1916번 최소비용 구히기

import sys
import heapq
import math

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  M = int(input())

  bus = [[100001 for _ in range(N)] for _ in range(N)]
  dist = [math.inf for _ in range(N)]

  for _ in range(M):
    dep, des, cost = map(int, input().split())

    bus[dep - 1][des - 1] = min(bus[dep - 1][des - 1], cost)

  start, end = map(int, input().split())
  start -= 1
  end -= 1

  heap = []
  dist[start] = 0

  heapq.heappush(heap, [0, start])

  while(heap):
    cost, at = heapq.heappop(heap)

    if dist[at] < cost:
      continue
    
    for i in range(N):
      if(bus[at][i] != 100001 and cost + bus[at][i] < dist[i]):
        dist[i] = cost + bus[at][i]
        heapq.heappush(heap, [dist[i], i])

  print(dist[end])
