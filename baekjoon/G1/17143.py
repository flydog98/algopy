# 17143번 낚시왕

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

class Shark:

  def __init__(self, s, d, z):
    self.speed = s
    self.direction = d
    self.size = z
  
  def move(self, y, x):
    global R, C
    nexty = y
    nextx = x

    # 위
    if(self.direction == 1):
      amount = self.speed % ((R - 1) * 2)
      nexty -= amount
      if(nexty < 0):
        nexty = (-nexty)
        self.direction = 2
        if(nexty >= R):
            nexty = (R - 1) - (nexty - (R - 1))
            self.direction = 1
    # 아래
    elif(self.direction == 2):
      amount = self.speed % ((R - 1) * 2)
      nexty += amount
      if(nexty >= R):
        nexty = (R - 1) - (nexty - (R - 1))
        self.direction = 1
        if(nexty < 0):
          nexty = (-nexty)
          self.direction = 2
    # 오른쪽
    elif(self.direction == 3):
      amount = self.speed % ((C - 1) * 2)
      nextx += amount
      if(nextx >= C):
        nextx = (C - 1) - (nextx - (C - 1))
        self.direction = 4
        if(nextx < 0):
          nextx = (-nextx)
          self.direction = 3
    # 왼쪽
    elif(self.direction == 4):
      amount = self.speed % ((C - 1) * 2)
      nextx -= amount
      if(nextx < 0):
        nextx = (-nextx)
        self.direction = 3
        if(nextx >= C):
            nextx = (C - 1) - (nextx - (C - 1))
            self.direction = 4

    return nexty, nextx

  def __str__(self):
    return f"({self.speed}, {self.direction}, {self.size})"

if __name__ == "__main__":
  global R, C
  R, C, M = map(int, input().split())
  answer = 0

  board = [[None for _ in range(C)] for _ in range(R)]

  for i in range(M):
    r, c, s, d, z = map(int, input().split())
    shark = Shark(s, d, z)
    board[r - 1][c - 1] = shark

  for i in range(C):
    # catch
    for y in range(R):
      if board[y][i] != None:
        answer += board[y][i].size
        board[y][i] = None
        break

    # move
    newmap = [[None for _ in range(C)] for _ in range(R)]
    for y in range(R):
      for x in range(C):
        if board[y][x] != None:
          shark = board[y][x]
          nexty, nextx = shark.move(y, x)
          if(newmap[nexty][nextx] == None):
            newmap[nexty][nextx] = shark
          else:
            if(newmap[nexty][nextx].size < shark.size):
              newmap[nexty][nextx] = shark
    
    board = newmap

    # print()
    # print(f"answer: {answer}")
    # for i in range(R):
    #   print(list(map(lambda x: x.__str__(), board[i])))

  print(answer)