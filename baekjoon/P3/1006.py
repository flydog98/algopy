# 1006번 습격자 초라기

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

'''
dp[i][0] - 서로 한 조 혹은 둘 다 이미 포함됨 -> i + 1에 영향 안 미침
dp[i][1] - 안쪽 i + 1과 한 조, 바깥쪽 모름
dp[i][2] - 바깥쪽 i + 1과 한 조, 안쪽 모름
dp[i][3] - 둘 다 i + 1과 한 조
모름: 이전 루프에서 포함되었을 수 있음
-1: 불가능
100000: 초기값
'''

INIT = 100000



def main():
    N, W = map(int, input().split())

    if(N == 1):
        a = int(input())
        b = int(input())
        if(a + b <= W):
            print(1)
        else:
            print(2)
        return

    enemy = [[] for _ in range(N)]
    for _ in range(2):
        _input = list(map(int, input().split()))
        for j in range(N):
            enemy[j].append(_input[j])

    def getdp():
        return [[INIT, INIT, INIT, INIT] for _ in range(N)]

    def go(dp):
        nonlocal N, W, enemy
        for at in range(1, N - 1):
            if(enemy[at][0] + enemy[at][1] <= W):
                dp[at][0] = min(dp[at - 1][0] + 1, dp[at - 1][1] + 1, dp[at - 1][2] + 1, dp[at - 1][3])
            else:
                dp[at][0] = min(dp[at - 1][0] + 2, dp[at - 1][1] + 1, dp[at - 1][2] + 1, dp[at - 1][3])
            if(enemy[at][0] + enemy[at + 1][0] <= W and dp[at][1] != -1):
                # 바깥쪽이 이전에 안 포함 vs 포함
                dp[at][1] = min(dp[at - 1][0] + 2, dp[at - 1][2] + 1)
            if(enemy[at][1] + enemy[at + 1][1] <= W and dp[at][2] != -1):
                # 안쪽이 이전에 안 포함 vs 포함
                dp[at][2] = min(dp[at - 1][0] + 2, dp[at - 1][1] + 1)
            if(enemy[at][0] + enemy[at + 1][0] <= W and enemy[at][1] + enemy[at + 1][1] <= W and dp[at][3] != -1):
                dp[at][3] = dp[at - 1][0] + 2

    answer = INIT

    # 안 겹치고 시작
    dp = getdp()
    if(enemy[0][0] + enemy[0][1] <= W):
        dp[0][0] = 1
    else:
        dp[0][0] = 2

    if(enemy[0][1] + enemy[1][1] <= W):
        dp[0][2] = 2
    if(enemy[0][0] + enemy[1][0] <= W):
        dp[0][1] = 2
    if(enemy[0][1] + enemy[1][1] <= W and enemy[0][0] + enemy[1][0] <= W):
        dp[0][3] = 2

    go(dp)
    if(enemy[N - 1][0] + enemy[N - 1][1] <= W):
        answer = min(answer, dp[N - 2][0] + 1, dp[N - 2][1] + 1, dp[N - 2][2] + 1, dp[N - 2][3])
    else:
        answer = min(answer, dp[N - 2][0] + 2, dp[N - 2][1] + 1, dp[N - 2][2] + 1, dp[N - 2][3])
    # 안쪽을 겹치고 시작
    if(enemy[0][0] + enemy[N - 1][0] <= W):
        dp = getdp()
        dp[0][0] = 2
        if(enemy[0][1] + enemy[1][1] <= W):
            dp[0][2] = 2
        dp[N - 2][1] = -1
        dp[N - 2][3] = -1
        go(dp)
        answer = min(answer, dp[N - 2][0] + 1, dp[N - 2][2])
    # 바깥쪽을 겹치고 시작
    if(enemy[0][1] + enemy[N - 1][1] <= W):
        dp = getdp()
        dp[0][0] = 2
        if(enemy[0][0] + enemy[1][0] <= W):
            dp[0][1] = 2
        dp[N - 2][2] = -1
        dp[N - 2][3] = -1
        go(dp)
        answer = min(answer, dp[N - 2][0] + 1, dp[N - 2][1])
    # 둘 다 겹치고 시작
    if(enemy[0][0] + enemy[N - 1][0] <= W and enemy[0][1] + enemy[N - 1][1] <= W):
        dp = getdp()
        dp[0][0] = 2
        dp[N - 2][1] = -1
        dp[N - 2][2] = -1
        dp[N - 2][3] = -1
        go(dp)
        answer = min(answer, dp[N - 2][0])

    print(answer)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        main()

