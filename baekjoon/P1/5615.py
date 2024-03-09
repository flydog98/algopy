# 5615번 아파트 임대

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

base = [2, 7, 61]


def power(x, y, p):
    if y < 2:
        return (x ** y) % p
    else:
        d = y // 2
        if y % 2 == 0:
            return (power(x, d, p) ** 2) % p
        else:
            return (x * (power(x, d, p)) ** 2) % p


def miller(n, a):
    if n <= 1:
        return False
    if n == 2:
        return True

    if n == a:
        return True

    k = n - 1
    r = 0

    while (k % 2 == 0):
        r += 1
        k = k // 2

    x = power(a, k, n)

    if x == 1 or x + 1 == n:
        return True

    for _ in range(r - 1):
        x = power(x, 2, n)
        if x + 1 == n:
            return True
    return False


def isPrime(n):
    for a in base:
        if (not miller(n, a)):
            return False
    return True


if __name__ == "__main__":
    N = int(input())
    ans = 0

    for _ in range(N):
        n = int(input())
        if (isPrime(2 * n + 1)):
            ans += 1

    print(ans)
