# 1520 내리막 길

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
dp = None
N = None
M = None

def dfs(board, visit, y, x):
  if(dp[y][x] != -1):
    return dp[y][x]

  if(y == N - 1 and x == M - 1):
    return 1
  
  visit[y][x] = 1
  dp[y][x] = 0

  for i in range(4):
    nextY = y + dy[i]
    nextX = x + dx[i]

    if(
      0 <= nextY < N and
      0 <= nextX < M and
      visit[nextY][nextX] == 0 and
      board[y][x] > board[nextY][nextX]
    ):
      dp[y][x] += dfs(board, visit, nextY, nextX)

  visit[y][x] = 0

  return dp[y][x]

if __name__ == "__main__":
  N, M = map(int, input().split())

  board = []
  dp = [[-1 for _ in range(M)] for _ in range(N)]
  visit = [[0 for _ in range(M)] for _ in range(N)]

  for i in range(N):
    board.append(list(map(int, input().split())))
  
  print(dfs(board, visit, 0, 0))
