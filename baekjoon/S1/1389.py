# 1389번 케빈 베이컨의 6단계 법칙

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
INF = 10000

if __name__ == '__main__':
  N, M = map(int, input().split())

  graph = [[INF for _ in range(N)] for _ in range(N)]

  for _ in range(M):
    a, b = map(int, input().split())

    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

  for via in range(N):
    for depart in range(N):
      for land in range(N):
        if(via != depart and via != land and depart != land):
          detour = graph[depart][via] + graph[via][land]
          if(graph[depart][land] > detour):
            graph[depart][land] = detour
            graph[land][depart] = detour
  
  kbsum = []

  for i in range(N):
    nowsum = 0
    for j in range(N):
      if(i != j):
        nowsum += graph[i][j]
    kbsum.append(nowsum)

  print(kbsum.index(min(kbsum)) + 1)
