# 1981번 배열에서 이동

# pypy로 통과

import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

x_dir = [-1, 1, 0, 0]
y_dir = [0, 0, -1, 1]

def isPossible(mid):
  i = 0
  while(i + mid <= 200):
    if bfs(i, i + mid):
      return True
    i += 1
  return False

def bfs(bot, top):
  global N, board

  if not(bot <= board[0][0] <= top):
    return False

  queue = [[0, 0]]
  visit = [[0] * N for _ in range(N)]
  visit[0][0] = 1

  while(queue):
    now = queue.pop(0)
    y = now[0]
    x = now[1]
    if y == N - 1 and x == N - 1:
      return True

    for i in range(4):
      nextx = x + x_dir[i]
      nexty = y + y_dir[i]

      if (0 <= nextx < N and 0 <= nexty < N):
        next_v = board[nexty][nextx]
        if (visit[nexty][nextx] == 0 and (bot <= next_v <= top)):
          visit[nexty][nextx] = 1
          queue.append([nexty, nextx])

  return False

if __name__ == "__main__":
  global N, board
  N = int(input())
  board = []

  for _ in range(N):
    board.append(list(map(int, input().split())))

  left = 0
  right = 200

  while(left <= right):
    mid = (left + right) // 2
    if isPossible(mid):
      right = mid - 1
    else:
      left = mid + 1

  print(left)
