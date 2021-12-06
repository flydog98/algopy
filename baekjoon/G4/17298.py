# 17298번 오큰수

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    answer = [-1] * n
    stack = []

    for i, number in enumerate(array):
        if stack:
            while stack and stack[-1][0] < number:
                popped = stack.pop()
                answer[popped[1]] = number
        stack.append((number, i))

    print(*answer, sep = ' ')
