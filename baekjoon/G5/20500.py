import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
  N = int(input())
  div = 1000000007

  end1 = [[0, 1, 0]]
  end5 = [[0, 0, 1]]

  for i in range(1, N):
    end1.append([
      (end1[i - 1][2] + end5[i - 1][2]) % div,
      (end1[i - 1][0] + end5[i - 1][0]) % div,
      (end1[i - 1][1] + end5[i - 1][1]) % div
    ])
    end5.append([
      (end1[i - 1][1] + end5[i - 1][1]) % div,
      (end1[i - 1][2] + end5[i - 1][2]) % div,
      (end1[i - 1][0] + end5[i - 1][0]) % div
    ])

  print(end5[N - 1][0])
  