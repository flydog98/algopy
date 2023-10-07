# 2098 외판원 순회

import sys
import math

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = None
isEnd = None
dp = None
cost = None

def tsp(now, visited):
  if(visited == isEnd):
    if(cost[now][0] == 0):
      return math.inf
    else:
      return cost[now][0]
  
  if(dp[now][visited] != 0):
    return dp[now][visited]
  
  dp[now][visited] = math.inf

  for i in range(N):
    if(cost[now][i] != 0 and visited & (1 << i) == 0):
      temp = tsp(i, visited | (1 << i))
      dp[now][visited] = min(dp[now][visited], cost[now][i] + temp)

  return dp[now][visited]

if __name__ == "__main__":
  N = int(input())
  isEnd = (1 << N) - 1
  dp = [[0 for _ in range(1 << 16)] for _ in range(16)]
  cost = []

  for i in range(N):
    cost.append(list(map(int, input().split())))

  print(tsp(0, 1))
