# 9376번 탈옥

import sys
from queue import Empty, PriorityQueue

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

gox = [1, -1, 0, 0]
goy = [0, 0, -1, 1]

def dfs(board, y, x, row, column):
  queue = PriorityQueue()
  queue.put((0,[y, x]))

  ret_board = [[10001] * (column + 2) for x in range(row + 2)]
  ret_board[y][x] = 0

  while(queue.qsize()):
    nowcount, loc = queue.get()
    nowy, nowx = loc
    
    for i in range(4):
      nextx = nowx + gox[i]
      nexty = nowy + goy[i]
      if (0 <= nextx and nextx < column + 2 and 0 <= nexty and nexty < row + 2 and ret_board[nexty][nextx] == 10001):
        nextvalue = board[nexty][nextx]
        if nextvalue == '.' or nextvalue == '$':
          ret_board[nexty][nextx] = nowcount
          queue.put((nowcount, [nexty, nextx]))
        elif nextvalue == '#':
          ret_board[nexty][nextx] = nowcount + 1
          queue.put((nowcount + 1, [nexty, nextx]))

  return ret_board

def main():
  row, column = map(int, input().split())
  topstr = "." * (column + 2)
  board = [list(topstr)]
  ans = 10001

  for _ in range(row):
    board.append(["."] + list(input().strip()) + ["."])
  board.append(list("" + topstr))

  flag = True
  res1 = dfs(board, 0, 0, row, column)
  for i in range(row + 2):
    for j in range(column + 2):
      if board[i][j] == '$':
        if flag:
          res2= dfs(board, i, j, row, column)
          flag = False
        else:
          res3= dfs(board, i, j, row, column)
      
  for i in range(row + 2):
    for j in range(column + 2):
      now = board[i][j]

      if now == '.' or now == '$':
        ans = min(ans, res1[i][j] + res2[i][j] + res3[i][j])
      elif now == '#':
        ans = min(ans, res1[i][j] + res2[i][j] + res3[i][j] - 2)

  print(ans)

if __name__ == "__main__":
  testcase = int(input())

  for _ in range(testcase):
    main()
