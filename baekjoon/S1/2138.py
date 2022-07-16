# 2138번 전구와 스위치

import sys
import copy

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  def switch_value(now, i):
    if now[i] == 1:
      now[i] = 0
    else:
      now[i] = 1
  
  def switch_range(now, i):
    switch_value(now, i)
    switch_value(now, i + 1)
    switch_value(now, i + 2)

  def process(N, now, final):
    ret = 0
    for i in range(N - 2):
      if now[i] != final[i]:
        switch_range(now, i)
        ret += 1
    if now[N - 2] != final[N - 2]:
      switch_value(now, N - 2)
      switch_value(now, N - 1)
      ret += 1
    
    return ret

  N = int(input())
  now1 = list(map(int, list(input().strip())))
  now2 = copy.deepcopy(now1)
  final = list(map(int, list(input().strip())))

  switch_value(now1, 0)
  switch_value(now1, 1)
  answer1 = process(N, now1, final) + 1
  answer2 = process(N, now2, final)

  flag1 = True
  flag2 = True
  for i in range(N):
    if now1[i] != final[i]:
      flag1 = False
    if now2[i] != final[i]:
      flag2 = False
  
  if flag1 and flag2:
    print(min(answer1, answer2))
  elif flag1:
    print(answer1)
  elif flag2:
    print(answer2)
  else:
    print(-1)
