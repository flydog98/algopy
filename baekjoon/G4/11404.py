# 11404번 플로이드

import sys
sys.setrecursionlimit(10**6)

INF = 1000000000

if __name__ == '__main__':
  city_amount = int(sys.stdin.readline())
  bus_amount = int(sys.stdin.readline())

  costs = [[INF for _ in range(city_amount)] for _ in range(city_amount)]
  for city in range(city_amount):
    costs[city][city] = 0

  for _ in range(bus_amount):
    start, end, cost = map(int, sys.stdin.readline().split())
    if costs[start - 1][end - 1] == 0 or costs[start - 1][end - 1] > cost:
      costs[start - 1][end - 1] = cost

  for waypoint in range(city_amount):
    for depart in range(city_amount):
      for land in range(city_amount):
        original = costs[depart][land]
        detourA = costs[depart][waypoint]
        detourB = costs[waypoint][land]
        detour = detourA + detourB

        if detour < original:
          costs[depart][land] = detour
  
  for depart in range(city_amount):
    for land in range(city_amount):
      if costs[depart][land] == INF:
        costs[depart][land] = 0

  for city in range(city_amount):
    print(*costs[city])
