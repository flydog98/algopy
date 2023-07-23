# 2254 감옥 건설

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def ccw(p1, p2, p3):
  return p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])

def monoton_chain(points):
  global x, y
  lower = []
  upper = []
  left = []

  for point in points:
    while (len(lower) > 1) and (ccw(lower[-2], lower[-1], point) < 0):
      lower.pop()
    lower.append(point)

  for point in reversed(points):
    while (len(upper) > 1) and (ccw(upper[-2], upper[-1], point) < 0):
      upper.pop()
    upper.append(point)

  convex = lower[:-1] + upper[:-1]

  for point in convex:
    if(point[0] == x and point[1] == y):
      return False

  for point in points:
    flag = True
    for included in convex:
      if(point[0] == included[0] and point[1] == included[1]):
        flag = False

    if(flag):
      left.append(point)

  return left

if __name__ == "__main__":
  global x, y
  N, x, y= map(int, input().split())

  points = []
  answer = 0

  points.append([x, y])
  for i in range(N):
    a, b = map(int, input().split())
    points.append([a, b])

  while(len(points) > 3):
    points.sort(key=lambda point: (point[0], point[1]))
    points = monoton_chain(points)
    if(points == False):
      break
    answer += 1

  print(answer)
  