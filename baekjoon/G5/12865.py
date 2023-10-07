import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N, K = map(int, input().split())

  bag = [0 for _ in range(K + 1)]

  for i in range(N):
    W, V = map(int, input().split())

    for j in range(K, 0, -1):
      if(j + W <= K and bag[j] and bag[j] + V > bag[j + W]):
        bag[j + W] = bag[j] + V

    if(W <= K):
      bag[W] = max(bag[W], V)

  print(max(bag))
