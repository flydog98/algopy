# 16236 아기 상어

import sys
import heapq

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(board, i, j):
  global size, eat, N

  visit = [[0 for _ in range(N)] for _ in range(N)]

  heap = []
  heapq.heappush(heap, [0, i, j])
  visit[i][j] = 1

  while(heap):
    move, y, x = heapq.heappop(heap)

    if(0 < board[y][x] < size):
      eat += 1
      board[y][x] = 0
      if eat == size:
        eat = 0
        size += 1

      return move, y, x

    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]

      if(
        0 <= ny < N and
        0 <= nx < N and
        visit[ny][nx] == 0 and
        board[ny][nx] <= size
      ):
        visit[ny][nx] = 1
        heapq.heappush(heap, [move + 1, ny, nx])

  return 0, i, j

if __name__ == "__main__":
  global N, size, eat
  N = int(input())
  size = 2
  eat = 0

  board = []
  y = 0; x = 0
  time = 0

  for _ in range(N):
    board.append(list(map(int, input().split())))

  for i in range(N):
    for j in range(N):
      if(board[i][j] == 9):
        y = i; x = j
        board[y][x] = 0

  while(True):
    cost, newy, newx = bfs(board, y, x)
    if(cost == 0):
      break

    y = newy; x = newx
    time += cost

  print(time)
  