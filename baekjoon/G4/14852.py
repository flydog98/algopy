# 14852 타일 채우기 3

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())

  ans = [0, 2, 7, 22]
  _sum = [1, 3, 10, 32]

  for i in range(4, N + 1):
    ans.append((ans[i - 1] * 2 + ans[i - 2] * 3 + _sum[i - 3] * 2) % 1000000007)
    _sum.append((_sum[i - 1] + ans[i]) % 1000000007)

  print(ans[N])
