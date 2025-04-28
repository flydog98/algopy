# 28278번 스택 2

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  stack = []

  for _ in range(N):
    line = list(map(int, input().split()))

    if line[0] == 1:
      stack.append(line[1])
    elif line[0] == 2:
      if stack:
        print(stack.pop())
      else:
        print(-1)
    elif line[0] == 3:
      print(len(stack))
    elif line[0] == 4:
      if stack:
        print(0)
      else:
        print(1)
    elif line[0] == 5:
      if stack:
        print(stack[-1])
      else:
        print(-1)
