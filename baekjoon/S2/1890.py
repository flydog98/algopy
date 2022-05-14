# 1890번 점프

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())

  board = []
  answer = [[0 for x in range(N)] for y in range(N)]

  for _ in range(N):
    board.append(list(map(int, input().split())))

  answer[0][0] = 1
  for y in range(N):
    for x in range(N):
      now = board[y][x]
      if(now):
        now_way = answer[y][x]

        if(y + now < N):
          answer[y + now][x] += now_way
        if(x + now < N):
          answer[y][x + now] += now_way
  
  print(answer[N - 1][N - 1])