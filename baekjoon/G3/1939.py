# 1939번 중량제한

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def bfs(mid):
  global roads, site1, site2, N

  queue = [site1]
  visit = [0] * (N + 1)
  visit[site1] = 1

  while(queue):
    now = queue.pop(0)
    if now == site2:
      return True

    for go in roads[now].items():
      next_p = go[0]
      weight = go[1]
      if weight >= mid and visit[next_p] == 0:
        visit[next_p] = 1
        queue.append(next_p)

  return False

if __name__ == "__main__":
  global roads, site1, site2, N
  N, M = map(int, input().split())
  roads = [{} for _ in range(N + 1)]

  for _ in range(M):
    A, B, C = map(int, input().split())
    if B not in roads[A]:
      roads[A][B] = C
      roads[B][A] = C
    else:
      roads[A][B] = max(roads[A][B], C)
      roads[B][A] = max(roads[B][A], C)
  
  left = 1
  right = 1000000000

  site1, site2 = map(int, input().split())

  while(left <= right):
    mid = (left + right) // 2
    if bfs(mid):
      left = mid + 1
    else:
      right = mid - 1

  print(right)
