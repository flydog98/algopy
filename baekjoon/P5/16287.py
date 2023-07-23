# 16287 Parcel

# pypy3으로 정답

import sys

input = sys.stdin.readline

def main():
  w, n = map(int, input().split())

  parcels = list(map(int, input().split()))

  twos = [0 for _ in range(w + 1)]

  for i in range(n):
    for j in range(i + 1, n):
      if (parcels[i] + parcels[j] <= w):
        twos[parcels[i] + parcels[j]] = [i, j]
  
  for i in range(n):
    for j in range(i + 1, n):
      weight = parcels[i] + parcels[j]
      if (weight <= w) and twos[w - weight]:
        if i not in twos[w - weight] and j not in twos[w - weight]:
          print("YES")
          return
  
  print("NO")
  return

if __name__ == "__main__":
  main()
