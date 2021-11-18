# 14725번 개미굴

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

class Node:
  def __init__(self, name):
    self.nexts = []
    self.name = name

  def input(self, food):
    for next_food in self.nexts:
      if(next_food.name == food):
        return
    self.nexts.append(Node(food))

  def find(self, food):
    for next_food in self.nexts:
      if(next_food.name == food):
        return next_food

  def sorting(self):
    self.nexts.sort(key = lambda x: x.name)
    for next_food in self.nexts:
      next_food.sorting()

  def printing(self, depth):
    if(depth > 0):
      print(f"{'--' * (depth - 1)}{self.name}")
    for next_food in self.nexts:
      next_food.printing(depth + 1)

if __name__ == "__main__":
  N = int(input())

  root = Node("")

  for _ in range(N):
    line = list(input().split())

    now = root
    for food in line[1:]:
      now.input(food)
      now = now.find(food)
  
  root.sorting()

  root.printing(0)
