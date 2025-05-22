# 14502 연구소

import sys
import copy

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = 0; M = 0

goy = [0, 0, -1, 1]
gox = [1, -1, 0, 0]

def calc(board):
  visit = [[0 for _ in range(M)] for _ in range(N)]

  for y in range(N):
    for x in range(M):
      if visit[y][x] == 0 and board[y][x] == 2:
        bfs = [[y, x]]
        visit[y][x] = 1
        while bfs:
          nowy, nowx = bfs.pop(0)

          for i in range(4):
            nexty = nowy + goy[i]
            nextx = nowx + gox[i]

            if (0 <= nexty < N) and \
                (0 <= nextx < M) and \
                (board[nexty][nextx] == 0) and \
                (visit[nexty][nextx] == 0):
              visit[nexty][nextx] = 1
              board[nexty][nextx] = 2
              bfs.append([nexty, nextx])

  safe = 0

  for y in range(N):
    for x in range(M):
      if board[y][x] == 0:
        safe += 1

  return safe

if __name__ == "__main__":
  N, M = map(int, input().split())
  board = []
  ans = 0
  
  for _ in range(N):
    board.append(list(map(int, input().split())))
  
  for a in range(N):
    for b in range(M):
      if board[a][b] != 0:
        continue
      for c in range(N):
        for d in range(M):
          if (c < a or (a == c and d <= b)) or board[c][d] != 0:
            continue
          for e in range(N):
            for f in range(M):
              if (e < c or (c == e and f <= d)) or board[e][f] != 0:
                continue
              temp_board = copy.deepcopy(board)
              temp_board[a][b] = 1
              temp_board[c][d] = 1
              temp_board[e][f] = 1
              ans = max(ans, calc(temp_board))

  print(ans)
