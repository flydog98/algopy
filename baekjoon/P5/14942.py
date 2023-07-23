# 14942 개미

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

class Ant:
  def __init__(self, number, energy):
    self.number = number
    self.energy = energy
    self.at = number

class Node:
  def __init__(self):
    self.ants = []
    self.visit = 0
    self.conn = []

def dfs(at):
  global n, tree, ants

  tree[at].visit = 1

  for (nodeNo, cost) in tree[at].conn:
    if(tree[nodeNo].visit == 0):
      dfs(nodeNo)
      for ant in tree[nodeNo].ants:
        if ant.energy >= cost:
          tree[at].ants.append(ant)
          ant.at = at
          ant.energy -= cost

if __name__ == "__main__":
  global n, tree, ants
  n = int(input())
  tree = [Node() for _ in range(n + 1)]
  ants = [0]

  for i in range(n):
    temp = int(input())
    ant = Ant(i + 1, temp)
    tree[i + 1].ants.append(ant)
    ants.append(ant)

  for i in range(n - 1):
    a, b, cost = map(int, input().split())
    tree[a].conn.append([b, cost])
    tree[b].conn.append([a, cost])

  dfs(1)

  for i in range(1, n + 1):
    print(ants[i].at)