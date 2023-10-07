# 14428 수열과 쿼리 16

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


class Node:
    def __init__(self, start, end, values):
        self.start = start
        self.end = end
        self.mid = int((start + end) / 2)

        self.left = None
        self.right = None

        self.min_index = -1
        self.min_value = -1

        if (self.start != self.end):
            self.left = Node(self.start, self.mid, values)
            self.right = Node(self.mid + 1, self.end, values)
            self.update_min()
        else:
            self.min_value = values[self.start]
            self.min_index = self.start

    def update_min(self):
        if (self.left.min_value <= self.right.min_value):
            self.min_value = self.left.min_value
            self.min_index = self.left.min_index
        else:
            self.min_value = self.right.min_value
            self.min_index = self.right.min_index

    def change(self, index, value):
        if (self.start == self.end and self.start == index):
            self.min_value = value
            return

        if (self.start <= index and index <= self.end):
            if (index <= self.mid):
                self.left.change(index, value)
            else:
                self.right.change(index, value)

            self.update_min()

    def get_min(self, start, end):
        if (start == self.start and self.end == end):
            return self.min_value, self.min_index

        if (self.mid < start):
            return self.right.get_min(start, end)
        if (end <= self.mid):
            return self.left.get_min(start, end)

        lv, li = self.left.get_min(start, self.mid)
        rv, ri = self.right.get_min(self.mid + 1, end)

        if (lv <= rv):
            return lv, li
        else:
            return rv, ri


if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    root = Node(0, n - 1, values)

    m = int(input())

    for _ in range(m):
        a, b, c = map(int, input().split())
        if (a == 1):
            root.change(b - 1, c)
        elif (a == 2):
            _, index = root.get_min(b - 1, c - 1)
            print(index + 1)
