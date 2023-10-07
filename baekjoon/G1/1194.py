# 1194 달이 차오른다, 가자.

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def main():
  N, M = map(int, input().split())
  board = []
  startx = 0; starty = 0
  visit = [[[0 for _ in range(1 << 6)] for _ in range(M)] for _ in range(N)]

  for _ in range(N):
    board.append(list(input().strip()))

  for i in range(N):
    for j in range(M):
      if(board[i][j] == '0'):
        starty = i
        startx = j
        board[i][j] = '.'

  queue = [[starty, startx, 0, 0]]
  visit[starty][startx][0] = 1

  while(queue):
    y, x, key, move = queue.pop(0)

    if(board[y][x] == '1'):
      print(move)
      return

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if(
        0 <= ny < N and
        0 <= nx < M and
        visit[ny][nx][key] == 0 and
        board[ny][nx] != '#'
      ):
        if(board[ny][nx] in ['.', '1']):
          visit[ny][nx][key] = 1
          queue.append([ny, nx, key, move + 1])
        elif(board[ny][nx] in ['a', 'b', 'c', 'd', 'e', 'f']):
          visit[ny][nx][key | (1 << (ord(board[ny][nx]) - ord('a')))] = 1
          queue.append([ny, nx, (key | (1 << (ord(board[ny][nx]) - ord('a')))), move + 1])
        elif(key & (1 << (ord(board[ny][nx]) - ord('A')))):
          visit[ny][nx][key | (1 << (ord(board[ny][nx]) - ord('A')))] = 1
          queue.append([ny, nx, (key | (1 << (ord(board[ny][nx]) - ord('A')))), move + 1])
        
  print(-1)

main()
