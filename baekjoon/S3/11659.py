# 11659번 구간 합 구하기 4

import sys

N, M = map(int, sys.stdin.readline().split())

sum = [0]
data = list(map(int, sys.stdin.readline().split()))

sum.append(data[0])
for i, number in enumerate(data[1:]):
  sum.append(sum[i + 1] + number)

for i in range(M):
  i, j = map(int, sys.stdin.readline().split())

  print(sum[j] - sum[i - 1])
