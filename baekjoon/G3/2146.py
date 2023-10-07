# 2146 다리 만들기

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

if __name__ == "__main__":
  N = int(input())
  board = []
  country = [[0 for _ in range(N)] for _ in range(N)]
  cnt = 1
  ans = 10000000

  for i in range(N):
    board.append(list(map(int, input().split())))

  for i in range(N):
    for j in range(N):
      if(board[i][j] == 1 and country[i][j] == 0):
        queue = [[i, j]]
        country[i][j] = cnt

        while(queue):
          y, x = queue.pop(0)

          for k in range(4):
            nextY = y + dy[k]
            nextX = x + dx[k]
            if(0 <= nextX < N and
               0 <= nextY < N and
               board[nextY][nextX] == 1 and
               country[nextY][nextX] == 0):
              
              country[nextY][nextX] = cnt
              queue.append([nextY, nextX])
      
        cnt += 1

  for i in range(N):
    for j in range(N):
      if(country[i][j] != 0):
        now = country[i][j]

        queue = [[i, j, 0]]
        visit = [[0 for _ in range(N)] for _ in range(N)]
        
        while(queue):
          y, x, bridge = queue.pop(0)

          for k in range(4):
            nextY = y + dy[k]
            nextX = x + dx[k]

            if(0 <= nextX < N and
              0 <= nextY < N and
              visit[nextY][nextX] == 0 and
              country[nextY][nextX] != 0 and
              country[nextY][nextX] != now):
              ans = min(ans, bridge)
              queue = []
              break

            if(0 <= nextX < N and
              0 <= nextY < N and
              visit[nextY][nextX] == 0 and
              country[nextY][nextX] == 0):
              visit[nextY][nextX] = 1
              queue.append([nextY, nextX, bridge + 1])

  print(ans)
  