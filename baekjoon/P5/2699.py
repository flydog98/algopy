# 2699 격자점 컨벡스헐

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def ccw(p1, p2, p3):
  return p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])

def monoton_chain(points):
  convex = []

  for point in points:
    while (len(convex) > 1) and (ccw(convex[-2], convex[-1], point) >= 0):
      convex.pop()
    convex.append(point)

  return convex[:-1]

def main():
  N = int(input())
  points = []

  for i in range(0, N, 5):
    inp = list(map(int, input().split()))
    for j in range(0, len(inp), 2):
      points.append([inp[j], inp[j + 1]])

  points.sort(key=lambda point: (-point[1], point[0]))

  upper = monoton_chain(points)
  lower = monoton_chain(reversed(points))

  print(len(lower) + len(upper))
  for p in upper:
    print(p[0], p[1])
  for p in lower:
    print(p[0], p[1])


if __name__ == "__main__":
  P = int(input())

  for i in range(P):
    main()
