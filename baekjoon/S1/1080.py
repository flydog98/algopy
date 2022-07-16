# 1080번 행렬

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  def get_matrix(N):
    ret = []
    for _ in range(N):
      temp = list(map(int, list(input().strip())))
      ret.append(temp)
    return ret

  def change_matrix(matrix, i, j):
    for y in range(3):
      for x in range(3):
        if matrix[i + y][j + x] == 1:
          matrix[i + y][j + x] = 0
        else:
          matrix[i + y][j + x] = 1

  N, M = map(int, input().split())
  A = get_matrix(N)
  B = get_matrix(N)
  answer = 0

  for i in range(N - 2):
    for j in range(M - 2):
      if A[i][j] != B[i][j]:
        change_matrix(A, i, j)
        answer += 1

  flag = True
  for i in range(N):
    for j in range(M):
      if A[i][j] != B[i][j]:
        flag = False

  if flag:
    print(answer)
  else:
    print(-1)