# 3584번 가장 가까운 공통 조상

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find(a, b):
  global N, parent, level

  if (level[a] < level[b]):
    a, b = b, a

  while(level[a] != level[b]):
    a = parent[a]

  while(a != b):
    a = parent[a]
    b = parent[b]

  return a

def dfs(a, lev):
  global parent, level, decendent

  level[a] = lev

  for dec in decendent[a]:
    dfs(dec, lev + 1)
  
def main():
  global N, parent, level, decendent
  N = int(input())
  parent = [-1 for x in range(N + 1)]
  decendent = [[] for _ in range(N + 1)]
  level = [0 for x in range(N + 1)]

  for _ in range(N - 1):
    a, b = map(int, input().split())
    parent[b] = a
    decendent[a].append(b)

  for i in range(1, N + 1):
    if parent[i] == -1:
      root = i
      break
  
  dfs(root, 0)

  a, b = map(int, input().split())
  print(find(a, b))

if __name__ == "__main__":
  tc = int(input())
  for _ in range(tc):
    main()
