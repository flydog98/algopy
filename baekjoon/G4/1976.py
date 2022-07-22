# 1976번 여행 가자

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find(at):
  global roads
  if roads[at] == at:
    return at
  
  roads[at] = find(roads[at])
  return roads[at]

def union(a, b):
  global roads, heights
  a = find(a)
  b = find(b)

  if a == b:
    return

  if heights[a] < heights[b]:
    roads[a] = b
  
  else:
    roads[b] = a
    if heights[a] == heights[b]:
      heights[a] += 1


if __name__ == "__main__":
  N = int(input())

  M = int(input())

  global roads, heights

  roads = [x for x in range(N)]
  heights = [1 for x in range(N)]

  for i in range(N):
    input_road = list(map(int, input().split()))

    for j in range(N):
      if j == i:
        continue
      
      if input_road[j] == 1:
        union(i, j)

  trip_plan = list(map(int, input().split()))

  root = find(trip_plan[0] - 1)
  flag = True

  for dest in trip_plan:
    if root != find(dest - 1):
      flag = False

  if flag:
    print("YES")
  else:
    print("NO")
