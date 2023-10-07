# 12969번 ABC

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N, K = map(int, input().split())

  maxK = int(N * (N - 1) / 2) + 1
  A, B, C = 0, 0, 0
  flag = True

  dp = [[[[0] * maxK for y in range(N + 1)] for z in range(N + 1)] for k in range(N + 1)]

  dp[1][1][0][0] = 1
  dp[1][0][1][0] = 1
  dp[1][0][0][0] = 1

  for i in range(2, N + 1):
    for a in range(N + 1):
      for b in range(N + 1):
        for k in range(maxK):
          if (a > 0 and dp[i - 1][a - 1][b][k] == 1) or (b > 0 and k >= a and dp[i - 1][a][b - 1][k - a] == 1) or (k >= a + b and dp[i - 1][a][b][k - a - b] == 1):
            dp[i][a][b][k] = 1
            if i == N and k == K:
              A = a
              B = b
              C = N - a - b
              flag = False

  if flag:
    print(-1)
  else:
    result = ""
    Cback = int(K / (A + B))

    if B == 0 and C == 0:
      result += "A" * A
    elif C == 0:
      midA = int(K / B)
      midB = int(K / A)
      Aback = K % A
      result += "B" * max(0, B - midB)
      result += "A" * midA
      result += "B" * max(0, (midB - 1))
      result += "A" * min(A, Aback)
      result += "B"
    else:
      Bback = K % (A + B)

      result += "C" * max(0, (C - Cback))
      result += "B" * max(0, (B - Bback))
      result += "A" * min(A, (Bback))
      result += "B" * min(B, (Bback))
      result += "A" * max(0, (A - Bback))
      result += "C" * min(C, (Cback))

    print(result)


"""
가능성 여부를 따지는 과정과
문자열을 찾아가는 과정 2개로 나뉜다.
가능성 여부를 따지는 곳에서는 시간 초과가 나고,
문자열 찾는 과정에서는 로직이 틀렸다.
"""
