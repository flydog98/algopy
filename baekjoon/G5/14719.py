# 14719 빗물

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  H, W = map(int, input().split())
  rain = 0

  blocks = list(map(int, input().split()))

  board = [[0 for _ in range(W)] for _ in range(H)]

  for j in range(W):
    block = blocks[j]
    for i in range(block):
      board[i][j] = 1

  for i in range(H):
    stack = 0
    started = False
    for j in range(W):
      if board[i][j] == 1:
        if started:
          rain += stack
          stack = 0
        else:
          started = True
      if board[i][j] == 0:
        if started:
          stack += 1
  
  print(rain)
  