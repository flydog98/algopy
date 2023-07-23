# 1708 볼록 껍질

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def ccw(p1, p2, p3):
  return p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])

def monoton_chain(points):
  convex = []

  for point in points:
    while (len(convex) > 1) and (ccw(convex[-2], convex[-1], point) <= 0):
      convex.pop()
    convex.append(point)

  return len(convex)

if __name__ == "__main__":
  N = int(input())
  points = []
  answer = 0

  for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

  points.sort(key=lambda point: (point[0], point[1]))

  answer += monoton_chain(points)
  answer += monoton_chain(reversed(points))

  print(answer - 2)
