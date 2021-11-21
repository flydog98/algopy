# 1504번 특정한 최단 경로

import sys
import heapq

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

INF = 8000000

def djickstra(start, end):
  global N, nodes
  distances = {node : INF for node in nodes}
  distances[start] = 0
  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue:
    now_dist, now_dest = heapq.heappop(queue)

    if distances[now_dest] < now_dist:
      continue
    
    for new_dest, new_dist in nodes[now_dest].items():
      dist = now_dist + new_dist
      if dist < distances[new_dest]:
        distances[new_dest] = dist
        heapq.heappush(queue, [dist, new_dest])
  
  if distances[end] == INF:
    raise Exception
  return distances[end]


if __name__ == "__main__":
  global N, nodes
  N, E = map(int, input().split())

  nodes = {x : dict() for x in range(N)}

  for _ in range(E):
    a, b, c = map(int, input().split())
    nodes[a - 1][b - 1] = c
    nodes[b - 1][a - 1] = c

  v1, v2 = map(int, input().split())

  try:
    dist_1_v1 = djickstra(0, v1 - 1)
    dist_1_v2 = djickstra(0, v2 - 1)

    dist_v1_v2 = djickstra(v1 - 1, v2 - 1)

    dist_v1_n = djickstra(v1 - 1, N - 1)
    dist_v2_n = djickstra(v2 - 1, N - 1)

    print(min(dist_1_v1 + dist_v2_n, dist_1_v2 + dist_v1_n) + dist_v1_v2)
  except:
    print(-1)
