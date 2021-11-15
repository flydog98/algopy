# 1799번 비숍

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def boardprint():
  print()
  global board
  for line in board:
    print(*line)
  
def get_diag(j, i):
  return j + i, N - 1 + j - i

def get_next(j, i):
  global N
  if(j >= N - 1 and i >= N - 1):
    return N, N
  if(j == N - 1 or i == 0):
    tempj, tempi = get_placed_next(j, i)
    return get_placed_next(tempj, tempi)
  return j + 1, i - 1

def get_placed_next(j, i):
  global N
  if(j >= N - 1 and i >= N - 1):
    return N, N
  if(j + i >= N - 1):
    return j + i - N + 2, N - 1
  return 0, j + i + 1

def place(j, i, now_bishop):
  global N, max_bishop, board, diag1, diag2

  d1, d2 = get_diag(j, i)

  if(j == N or i == N):
    return
  
  if(board[j][i] == 1):
    if(diag1[d1] == 0 and diag2[d2] == 0):
      # 비숍을 배치
      diag1[d1] = 1
      diag2[d2] = 1
      board[j][i] = 2

      # 최댓값 업데이트
      if(now_bishop + 1 > max_bishop):
        max_bishop = now_bishop + 1

      # boardprint()

      # 다음 칸으로 진행
      tempj, tempi = get_placed_next(j, i)
      nextj, nexti = get_placed_next(tempj, tempi)
      place(nextj, nexti, now_bishop + 1)

      # 비숍을 뺌
      diag1[d1] = 0
      diag2[d2] = 0
      board[j][i] = 1
  
  # 다음 칸으로 진행
  nextj, nexti = get_next(j, i)
  place(nextj, nexti, now_bishop)

if __name__ == "__main__":
  global N, max_bishop, board, diag1, diag2
  N = int(input())
  max_bishop = 0
  result = 0

  board = []
  diag1 = [0 for _ in range(N * 2 - 1)]
  diag2 = [0 for _ in range(N * 2 - 1)]

  for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)

  place(0, 0, 0)
  result += max_bishop

  if(N > 1):
    max_bishop = 0
    place(0, 1, 0)
    result += max_bishop

  print(result)
  