# 9527번 소수의 연속합

import sys
import math

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def is_prime(n):
    ret = [True] * (n + 1)
    ret[0] = False
    ret[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if(ret[i] == True):
            now = i * 2
            while now <= n:
                ret[now] = False
                now += i

    return ret

def main():
    N = int(input())

    ans = 0

    prime = []
    for number, v in enumerate(is_prime(4000000)):
        if v:
            prime.append(number)
    
    start = 0
    end = 0
    now = 2

    while(True):
        if(now == N):
            ans += 1
        if(now < N):
            end += 1
            if(end == len(prime)):
                break
            now += prime[end]
        else:
            now -= prime[start]
            start += 1

    print(ans)

if __name__ == "__main__":
    main()
