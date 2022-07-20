# 1717번 집합의 표현

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find(sets, at):
  if sets[at] == at:
    return at

  sets[at] = find(sets, sets[at])
  return sets[at]

def union(sets, heights, a, b):
  a = find(sets, a)
  b = find(sets, b)

  if a == b:
    return

  if heights[a] < heights[b]:
    sets[a] = b
  else:
    sets[b] = a
    if a == b:
      heights[a] += 1

if __name__ == "__main__":
  n, m = map(int, input().split())

  sets = [x for x in range(n + 1)]
  heights = [1 for x in range(n + 1)]

  for _ in range(m):
    sign, a, b = map(int, input().split())

    if sign == 0:
      # 합집합
      union(sets, heights, a, b)

    else:
      # 포함 여부 확인
      if find(sets, a) == find(sets, b):
        print("YES")
      else:
        print("NO")
