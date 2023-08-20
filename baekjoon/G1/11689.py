# 11689 GCD(n, k) = 1

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    answer = n

    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            while (n % i == 0):
                n = n // i

            answer -= int(answer / i)

    if n > 1:
        answer -= int(answer / n)

    print(answer)
