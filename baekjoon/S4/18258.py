# 18258 큐2

import sys
import collections

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  queue = collections.deque()
  n = 0

  for _ in range(N):
    line = list(input().split())
    order = line[0]

    if order == "push":
      queue.append(int(line[1]))
      n += 1
    elif order == "pop":
      if queue:
        print(queue.popleft())
        n -= 1
      else:
        print(-1)
    elif order == "size":
      print(n)
    elif order == "empty":
      if n != 0:
        print(0)
      else:
        print(1)
    elif order == "front":
      if n != 0:
        print(queue[0])
      else:
        print(-1)
    elif order == "back":
      if n != 0:
        print(queue[-1])
      else:
        print(-1)
