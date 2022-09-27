# 11437번 LCA

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find(a, b):
  global N, parent, level

  if (level[a] < level[b]):
    a, b = b, a

  dif = level[a] - level[b]

  for i in range(20):
    if dif == 0:
      break
    if dif % 2 == 1:
      a = parent[a][i]
    dif = int(dif / 2)

  if (a != b):
    for i in range(19, -1, -1):
      if(parent[a][i] != -1 and parent[a][i] != parent[b][i]):
        a = parent[a][i]
        b = parent[b][i]
    a = parent[a][0]

  return a

def dfs(a, par):
  global N, parent, adj, level
  if a != 1:
    parent[a][0] = par
  level[a] = level[par] + 1

  for k in range(1, 20):
    if parent[a][k - 1] != -1:
      parent[a][k] = parent[parent[a][k - 1]][k - 1]

  for ad in adj[a]:
    if ad != par:
      dfs(ad, a)

def main():
  global N, parent, adj, level
  N = int(input())
  parent = [[-1] * 20 for x in range(N + 1)]
  adj = [[] for x in range(N + 1)]
  level = [0 for x in range(N + 1)]

  for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

  dfs(1, 0)

  M = int(input())

  for _ in range(M):
    a, b = map(int, input().split())
    print(find(a, b))

if __name__ == "__main__":
  main()
