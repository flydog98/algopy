# 2630번 색종이 만들기

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def cut(paper, startY, startX, size):
  global ans
  n = size // 2
  ran = [
    [startY, startX],
    [startY + n, startX],
    [startY, startX + n],
    [startY + n, startX + n]
    ]

  for k in range(4):
    now = paper[ran[k][0]][ran[k][1]]
    flag = False
    for i in range(ran[k][0], ran[k][0] + n):
      for j in range(ran[k][1], ran[k][1] + n):
        if(paper[i][j] != now):
          flag = True
          break
      if flag:
        break
    if(flag):
      cut(paper, ran[k][0], ran[k][1], n)
    else:
      ans[now] += 1

if __name__ == "__main__":
  global ans
  N = int(input())

  ans = [0, 0]
  paper = []

  for _ in range(N):
    paper.append(list(map(int, input().split())))

  now = paper[0][0]
  flag = False
  for i in range(N):
    for j in range(N):
      if(paper[i][j] != now):
        flag = True
        break
    if(flag):
      break
  
  if(flag):
    cut(paper, 0, 0, N)
  else:
    ans[now] += 1

  print(ans[0])
  print(ans[1])
