# 18870 좌표 압축

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  line = list(map(int, input().split()))
  numbers = []
  mini = {}

  for i in range(N):
    numbers.append([line[i], i, i])

  numbers
  sorted_numbers = sorted(numbers, key=lambda x: x[0])
  count = 0

  for number in sorted_numbers:
    if number[0] in mini:
      number[2] = mini[number[0]]
    else:
      mini[number[0]] = count
      number[2] = count
      count += 1

  sorted_numbers.sort(key=lambda x: x[1])

  ans = []
  for number in sorted_numbers:
    ans.append(number[2])

  print(*ans)
