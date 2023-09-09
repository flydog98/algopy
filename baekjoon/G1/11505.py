# 11505 구간 곱 구하기

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
VAL = 1000000007


class Node:
    def __init__(self, start, end, values):
        self.start = start
        self.end = end
        self.mid = int((start + end) / 2)

        self.left = None
        self.right = None

        if (self.start != self.end):
            self.left = Node(self.start, self.mid, values)
            self.right = Node(self.mid + 1, self.end, values)
            self.value = (self.left.value * self.right.value) % VAL
        else:
            self.value = values[self.start]

    def change(self, index, value):
        if (self.start == self.end and self.start == index):
            self.value = value
            return

        if (self.start <= index and index <= self.end):
            if (index <= self.mid):
                self.left.change(index, value)
            else:
                self.right.change(index, value)
            self.value = (self.left.value * self.right.value) % VAL

    def get_value(self, start, end):
        if (start == self.start and self.end == end):
            return self.value

        if (self.mid < start):
            return self.right.get_value(start, end)
        if (end <= self.mid):
            return self.left.get_value(start, end)

        lv = self.left.get_value(start, self.mid)
        rv = self.right.get_value(self.mid + 1, end)

        return (lv * rv) % VAL


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    values = []

    for _ in range(n):
        values.append(int(input()))

    root = Node(0, n - 1, values)

    for _ in range(m + k):
        a, b, c = map(int, input().split())
        if (a == 1):
            root.change(b - 1, c)
        elif (a == 2):
            value = root.get_value(b - 1, c - 1)
            print(value)
