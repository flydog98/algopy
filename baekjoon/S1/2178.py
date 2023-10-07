# 2178번 미로 탐색

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

if __name__ == "__main__":
  N, M = map(int, input().split())

  board = [[] for _ in range(N)]
  visit = [[0 for _ in range(M)] for _ in range(N)]

  for i in range(N):
    line = input().strip()

    for ch in line:
      board[i].append(int(ch))

  queue = [[0, 0, 1]]

  while(queue):
    y, x, move = queue.pop(0)

    if(y == N - 1 and x == M - 1):
      print(move)
      break

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if(
        0 <= ny < N and
        0 <= nx < M and
        visit[ny][nx] == 0 and
        board[ny][nx] == 1
      ):
        visit[ny][nx] = 1
        queue.append([ny, nx, move + 1])
