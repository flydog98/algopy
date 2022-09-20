# 5557번 1학년

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())

  numbers = list(map(int, input().split()))
  dp = [[0] * 21 for x in range(101)]
  dp[0][numbers[0]] = 1

  for i in range(1, N - 1):
    number = numbers[i]
    if number == 0:
      for j in range(21):
        dp[i][j] = 2 * dp[i - 1][j]
    else:
      for j in range(21):
        if j - number >= 0:
          dp[i][j] += dp[i - 1][j - number]
        if j + number <= 20:
          dp[i][j] += dp[i - 1][j + number]

  print(dp[N - 2][numbers[-1]])
