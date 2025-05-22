# 4779 칸토어 집합

if __name__ == "__main__":
  ans = []
  ans.append("-")
  for i in range(1, 13):
    ans.append(ans[i - 1] + " " * len(ans[i - 1]) + ans[i - 1])
  while True:
    try:
      N = int(input())

      print(ans[N])
    except EOFError:
      break
  