# 20009 형곤이의 소개팅

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


class Man:
    def __init__(self, name, number):
        self.lover = []
        self.engage = None
        self.loverPointer = 0
        self.name = name
        self.number = number


class Woman:
    def __init__(self, name, number):
        self.lover = []
        self.lovevalue = []
        self.engage = None
        self.name = name
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
    menNames = input().strip().split()
    womenNames = input().strip().split()
    men = []
    women = []
    menDict = {}
    womenDict = {}
    solomen = []

    for i in range(N):
        man = Man(menNames[i], i)
        men.append(man)
        solomen.append(man)
        menDict[menNames[i]] = man

        woman = Woman(womenNames[i], i)
        women.append(woman)
        womenDict[womenNames[i]] = woman        

    for i in range(N):
        temp = input().strip().split()
        name = temp[0]
        lovers = temp[1:]
        for j in range(N):
            menDict[name].lover.append(womenDict[lovers[j]])

    for i in range(N):
        temp = input().strip().split()
        name = temp[0]
        lovers = temp[1:]
        for j in range(N):
            womenDict[name].lover.append(menDict[lovers[j]])

    for i in range(N):
        woman = women[i]
        woman.lovevalue = [0 for _ in range(N)]
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

    for i in range(N):
        print(men[i].name, men[i].engage.name)
