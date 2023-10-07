# 27985 멘토링 매칭

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


class High:
    def __init__(self, number):
        self.prefer = []
        self.match = None
        self.preferPointer = 0
        self.number = number


class Univ:
    def __init__(self, number):
        self.prefervalue = []
        self.match = None
        self.number = number

    def preferred(self, high):
        if self.match == None:
            self.match = high
            return True, None
        if self.prefervalue[high.number] < self.prefervalue[self.match.number]:
            temp = self.match
            self.match = high
            return True, temp
        else:
            return False, high


if __name__ == "__main__":
    N = int(input())
    univs = [Univ(x) for x in range(N + 1)]
    highs = [High(x) for x in range(N + 1)]
    unmatched = []

    for i in range(1, N + 1):
        unmatched.append(highs[i])

    for i in range(1, N + 1):
        prefers = list(map(int, input().split()))
        for j in range(N):
            highs[i].prefer.append(univs[prefers[j]])

    for i in range(1, N + 1):
        univ = univs[i]
        univ.prefervalue = [0 for _ in range(N + 1)]
        up = N
        down = 1
        value = 1
        while (up >= down):
            if (abs(i - up) <= abs(i - down)):
                univ.prefervalue[down] = value
                down += 1
            else:
                univ.prefervalue[up] = value
                up -= 1
            value += 1

    while (unmatched):
        high = unmatched.pop(0)
        while (True):
            univ = high.prefer[high.preferPointer]
            res, loser = univ.preferred(high)
            high.preferPointer += 1
            if (res):
                high.match = univ
                if loser:
                    loser.match = None
                    unmatched.append(loser)
                break

    print(" ".join(list(map(lambda high: str(high.match.number), highs[1:]))))
