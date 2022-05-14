# 13398번 연속합 2

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  numbers = list(map(int, input().split()))

  series = [0 for x in range(N)]
  disconnect = [0 for x in range(N)]

  if(N == 1):
    print(numbers[0])

  else :
    series[0] = numbers[0]
    disconnect[0] = 0
    series[1] = max(series[0] + numbers[1], numbers[1])
    disconnect[1] = series[0]
  
    for i in range(2, N):
      series[i] = max(series[i - 1] + numbers[i], numbers[i])
      disconnect[i] = max(disconnect[i - 1] + numbers[i], series[i - 1])

    answer = series[0]

    for i in range(1, N):
      answer = max(answer, series[i], disconnect[i])

    print(answer)