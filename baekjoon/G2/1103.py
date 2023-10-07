# 1103번 게임

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

gox = [-1, 1, 0, 0]
goy = [0, 0, -1, 1]

def process(x):
  if "0" <= x and x <= "9":
    return int(x)
  return x

def dfs(y, x, value):
  global N, M, board, visit, store

  if visit[y][x] == 1:
    return -1
  
  if value + 1 <= store[y][x]:
    return 0
  
  visit[y][x] = 1
  store[y][x] = value + 1

  for i in range(4):
    nextx = x + gox[i] * board[y][x]
    nexty = y + goy[i] * board[y][x]

    if (0 <= nextx and nextx < M and 0 <= nexty and nexty < N and board[nexty][nextx] != 'H'):
      if dfs(nexty, nextx, value + 1) == -1:
        return -1
    
  visit[y][x] = 0


if __name__ == "__main__":
  global N, M, board, visit, store
  N, M = map(int, input().split())

  board = list()
  visit = [[0 for _ in range(M)] for _ in range(N)]
  store = [[0 for _ in range(M)] for _ in range(N)]

  for i in range(N):
    temp = list(map(process, list(input().strip())))
    board.append(temp)

  if dfs(0, 0, 0) == -1:
    print(-1)
  else:
    ans = 0
    for line in store:
      for value in line:
        ans = max(ans, value)
    print(ans)
