# 10610번 30

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  number = list(map(int, input().strip()))
  number.sort(reverse=True)
  if(sum(number) % 3 != 0 or number[-1] != 0):
    print(-1)
  else:
    print("".join(str(_) for _ in number))
