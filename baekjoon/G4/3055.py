# 3055번 탈출

from copy import deepcopy
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

nexty = [0, 0, -1, 1]
nextx = [1, -1, 0, 0]

def print_b(board):
  for x in board:
    print(x)

if __name__ == "__main__":
  row, column = map(int, input().split())
  board = []
  visit = [[0 for x in range (column)] for y in range(row)]
  start = [0, 0]
  watermove = 0

  def process():
    global board, row, column, watermove
    newboard = deepcopy(board)
    for y in range(row):
      for x in range(column):
        if(board[y][x] == '*'):
          for temp in range(4):
            goy = y + nexty[temp]
            gox = x + nextx[temp]

            if(0 <= goy and goy <= row - 1 and \
              0 <= gox and gox <= column - 1 and \
                newboard[goy][gox] == '.'):
                newboard[goy][gox] = '*'

    board = deepcopy(newboard)
    watermove += 1

  for _ in range(row):
    board.append(list(input().strip()))

  for y in range(row):
    for x in range(column):
      if(board[y][x] == 'S'):
        start = [y, x]
        board[y][x] = '.'
        visit[y][x] = 1

  queue = []

  queue.append([0, start])

  process()

  while(queue):
    move, now = queue.pop(0)

    if(move >= watermove):
      process()

    if(board[now[0]][now[1]] == 'D'):
      print(move)
      break

    for temp in range(4):
      goy = now[0] + nexty[temp]
      gox = now[1] + nextx[temp]

      if(0 <= goy and goy <= row - 1 and \
        0 <= gox and gox <= column - 1 and \
        board[goy][gox] != '*' and board[goy][gox] != 'X' and \
        visit[goy][gox] == 0):
        visit[goy][gox] = 1
        queue.append([move + 1, [goy, gox]])

  else:
    print("KAKTUS")
