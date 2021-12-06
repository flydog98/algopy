# 5014번 스타트링크

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def main():
    F, S, G, U, D = map(int, input().split())

    short = [-1] * (F + 1)
    queue = []

    queue.append(S)
    short[S] = 0

    while queue:
        now = queue.pop(0)
        nowmove = short[now]

        if(now == G):
            print(nowmove)
            return

        if(now + U <= F and short[now + U] == -1):
            queue.append(now + U)
            short[now + U] = nowmove + 1
        if(now - D >= 1 and short[now - D] == -1):
            queue.append(now - D)
            short[now - D] = nowmove + 1

    print("use the stairs")
    return

if __name__ == "__main__":
    main()
