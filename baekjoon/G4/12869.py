# 12869번 뮤탈리스크

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  hp = list(map(int, input().split()))

  if N == 1:
    if hp[0] % 9 == 0:
      print(int(hp[0] / 9))
    else:
      print(int(hp[0] / 9) + 1)

  elif N == 2:
    dp = [[0] * 61 for x in range(61)]
    dp[0][0] = 0
    for i in range(hp[0] + 1):
      for j in range(hp[1] + 1):
        if i == 0 and j == 0:
          continue
        dp[i][j] = min(dp[max(0, i - 9)][max(0, j - 3)], dp[max(0, i - 3)][max(0, j - 9)]) + 1
    print(dp[hp[0]][hp[1]])
  
  else:
    dp = [[[0] * 61 for x in range(61)] * 61 for y in range(61)]
    dp[0][0][0] = 0

    for i in range(hp[0] + 1):
      for j in range(hp[1] + 1):
        for k in range(hp[2] + 1):
          if i == 0 and j == 0 and k == 0:
            continue
          dp[i][j][k] = min(dp[max(0, i - 9)][max(0, j - 3)][max(0, k - 1)], dp[max(0, i - 9)][max(0, j - 1)][max(0, k - 3)], dp[max(0, i - 3)][max(0, j - 9)][max(0, k - 1)], dp[max(0, i - 1)][max(0, j - 9)][max(0, k - 3)], dp[max(0, i - 3)][max(0, j - 1)][max(0, k - 9)], dp[max(0, i - 1)][max(0, j - 3)][max(0, k - 9)]) + 1
    print(dp[hp[0]][hp[1]][hp[2]])      
