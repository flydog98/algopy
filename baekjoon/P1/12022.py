# 12022 짝

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


class Man:
    def __init__(self, number):
        self.lover = []
        self.engage = None
        self.loverPointer = 0
        self.number = number


class Woman:
    def __init__(self, number):
        self.lover = []
        self.lovevalue = []
        self.engage = None
        self.number = number

    def proposed(self, man):
        if self.engage == None:
            self.engage = man
            return True, None
        if self.lovevalue[man.number] < self.lovevalue[self.engage.number]:
            temp = self.engage
            self.engage = man
            return True, temp
        else:
            return False, man


if __name__ == "__main__":
    N = int(input())
    men = [Man(x) for x in range(N + 1)]
    women = [Woman(x) for x in range(N + 1)]
    solomen = []
    for i in range(1, N + 1):
        solomen.append(men[i])

    for i in range(N):
        numbers = list(map(int, input().split()))
        for j in range(N):
            men[i + 1].lover.append(women[numbers[j]])

    for i in range(N):
        numbers = list(map(int, input().split()))
        for j in range(N):
            women[i + 1].lover.append(men[numbers[j]])

    for i in range(1, N + 1):
        woman = women[i]
        woman.lovevalue = [0 for _ in range(N + 1)]
        for i, man in enumerate(woman.lover):
            man.number
            woman.lovevalue[man.number] = i

    while (solomen):
        soloman = solomen.pop(0)
        while (True):
            woman = soloman.lover[soloman.loverPointer]
            res, loser = woman.proposed(soloman)
            soloman.loverPointer += 1
            if (res):
                soloman.engage = woman
                if loser:
                    loser.engage = None
                    solomen.append(loser)
                break
    
    for i in range(1, N + 1):
        print(men[i].engage.number)
