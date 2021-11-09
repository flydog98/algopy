# 20040번 사이클 게임

import sys
sys.setrecursionlimit(10**6)

def find(number, parent):
  if(number == parent[number]):
    return number

  parent[number] = find(parent[number], parent)
  return parent[number]

def union(a, b, parent, level):
  u = find(a, parent)
  v = find(b, parent)

  if(u == v):
    return True
  
  if level[u] > level[v]:
    parent[u] = v
  else:
    parent[v] = u
  
  if(level[u] == level[v]):
    level[v] += 1
  
  return False

if __name__ == '__main__':
  N, M = map(int, sys.stdin.readline().split())

  parent = [x for x in range(N)]
  level = [1 for _ in range(N)]

  for count in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if union(a, b, parent, level):
      print(count + 1)
      break
  else:
    print(0)
