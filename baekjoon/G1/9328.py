# 9328번 열쇠

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')
gap = A - a

ymove = [0, 0, -1, 1]
xmove = [1, -1, 0, 0]

def solution():
  global board, visit, key, locqueue, waiting, answer
  row, column = map(int, input().split())
  board = []
  for _ in range(row):
    board.append(list(input().strip()))
  key = set(input().strip())

  locqueue = []
  visit = [[0 for x in range(column)] for y in range(row)]
  waiting = [[] for _ in range(26)]
  answer = 0

  def haskey(doorname):
    if doorname.lower() in key:
      return True
    else:
      return False

  def process(y, x):
    global visit, board, key, locqueue, waiting, answer

    if(visit[y][x] == 1):
      return

    nowvalue = board[y][x]
    noword = ord(nowvalue)
    nowloc = [y, x]

    if(nowvalue == '.'):
      locqueue.append(nowloc)
      visit[y][x] = 1

    if(nowvalue == '$'):
      locqueue.append(nowloc)
      visit[y][x] = 1
      answer += 1

    if(A <= noword <= Z):
      if(haskey(nowvalue)):
        locqueue.append(nowloc)
        visit[y][x] = 1
      else:
        waiting[noword - A].append(nowloc)
    
    if(a <= noword <= z):
      key.add(nowvalue)
      for waitee in waiting[noword - a]:
        locqueue.append(waitee)
      locqueue.append(nowloc)
      visit[y][x] = 1

  for y in range(row):
    if(y == 0 or y == row - 1):
      for x in range(column):
        process(y, x)
    else:
      process(y, 0)
      process(y, column - 1)
  
  while(locqueue):
    y, x = locqueue.pop(0)

    for temp in range(4):
      goy = y + ymove[temp]
      gox = x + xmove[temp]

      if(0 <= goy and goy <= row - 1) and \
        (0 <= gox and gox <= column - 1):
        process(goy, gox)

  print(answer)

for _ in range(int(input())):
  solution()
