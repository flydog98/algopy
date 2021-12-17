# 1937번 욕심쟁이 판다

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

goxs = [-1, 1, 0, 0]
goys = [0, 0, -1, 1]

n = int(input())

forest = []
counts = [[-1 for _ in range(n)] for _ in range(n)]

def dfs(i, j):
    now = forest[i][j]
    res = [0]

    for y, x in zip(goys, goxs):
        gox = j + x
        goy = i + y
        if(0 <= gox and gox < n and 0 <= goy and goy < n):
            if(forest[goy][gox] > now):
                if counts[goy][gox] == -1:
                    res.append(dfs(goy, gox) + 1)
                else:
                    res.append(counts[goy][gox] + 1)
    
    counts[i][j] = max(res)
    return counts[i][j]

def main():
    for _ in range(n):
        line = list(map(int, input().split()))
        forest.append(line)

    for i in range(n):
        for j in range(n):
            if counts[i][j] == -1:
                dfs(i, j)

    print(max(map(max, counts)) + 1)

if __name__ == "__main__":
    main()
