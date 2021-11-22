# 23560번 약

"""
00 1//1 00  0 -> 3, 2
00 1//0 01  1 -> 4, 0
00 1//0 10  2 -> 5, 1
01 0//1 00  3 -> 6, 5
01 0//0 01  4 -> 7, 3
01 0//0 10  5 -> 8, 4
10 0//1 00  6 -> 0, 8
10 0//0 01  7 -> 1, 6
10 0//0 10  8 -> 2, 7
"""

import sys

if __name__ == '__main__':
  N = int(sys.stdin.readline())
  way = 0
  now = [0, 0, 0, 0, 0, 1, 0, 0, 0]
  go = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  for meal in range(N * 3 - 2):
    if(meal % 3 == 1): # 점심
      #1
      go[0] += now[1]
      #4
      go[3] += now[4]
      #6
      go[0] += now[6]
      #7
      go[1] += now[7]
      go[6] += now[7]
      #8
      go[2] += now[8]
    else: # 아침저녁
      #0
      go[2] += now[0]
      go[3] += now[0]
      #1
      go[4] += now[1]
      #2
      go[5] += now[2]
      go[1] += now[2]
      #3
      go[6] += now[3]
      go[5] += now[3]
      #4
      go[7] += now[4]
      #5
      go[8] += now[5]
      go[4] += now[5]
      #6
      go[8] += now[6]
      #8
      go[7] += now[8]
    for i, go_ in enumerate(go):
      now[i] = go_
    go = [0, 0, 0, 0, 0, 0, 0, 0, 0]

  print(sum(now))
