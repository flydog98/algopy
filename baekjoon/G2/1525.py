# 1525번 퍼즐

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

gox = [1, -1, 0, 0]
goy = [0, 0, -1, 1]

def getmultiplier(y, x):
  return 10 ** (8 - 3 * y - x)

def main():
  puzzle = 0
  for i in range(3):
    for text in input().split():
      if text == "0":
        text = "9"
      puzzle *= 10
      puzzle += int(text)
  
  record = {puzzle : 0}
  queue = []
  queue.append(puzzle)

  while(queue):
  # for k in range(10):
    now = queue.pop(0)
    count = record[now]

    if now == 123456789:
      print(record[now])
      return

    loc = str(now).find("9")
    x = loc % 3
    y = loc // 3
    for i in range(4):
      nextx = x + gox[i]
      nexty = y + goy[i]

      if (0 <= nextx and nextx < 3 and 0 <= nexty and nexty < 3):
        nextpuzzle = now
        target = int(str(now)[3 * nexty + nextx])
        nextpuzzle -= 9 * getmultiplier(y, x)
        nextpuzzle -= target * getmultiplier(nexty, nextx)
        nextpuzzle += target * getmultiplier(y, x)
        nextpuzzle += 9 * getmultiplier(nexty, nextx)
        if nextpuzzle not in record:
          # print(now, " -> ", nextpuzzle, " count: ", count + 1)
          record[nextpuzzle] = count + 1
          queue.append(nextpuzzle)
          # print(queue)
    
  print(-1)

if __name__ == "__main__":
  import time
  start = time.time()
  main()
  print(time.time() - start)
