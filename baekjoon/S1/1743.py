# 1743 음식물 피하기

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

goy = [-1, 1, 0, 0]
gox = [0, 0, -1, 1]

if __name__ == "__main__":
  N, M, K = map(int, input().split())
  board = [[-1 for _ in range(M)] for _ in range(N)]
  ans = 0

  for _ in range(K):
    r, c = map(int, input().split())

    board[r - 1][c - 1] = 0

  for y in range(N):
    for x in range(M):
      if board[y][x] == 0:
        bfs = [[y, x]]
        board[y][x] = 1
        temp_ans = 0

        while(bfs):
          nowy, nowx = bfs.pop(0)
          temp_ans += 1
          for i in range(4):
            nexty = nowy + goy[i]
            nextx = nowx + gox[i]

            if (0 <= nexty < N and
                0 <= nextx <M and
                board[nexty][nextx] == 0):
              board[nexty][nextx] = 1
              bfs.append([nexty, nextx])
        ans = max(ans, temp_ans)

  print(ans)
