# 4195번 친구 네트워크

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find(network, name):
  if network[name] == name:
    return name
  
  network[name] = find(network, network[name])
  return network[name]

def union(network, friends_amount, a, b):
  a = find(network, a)
  b = find(network, b)

  if a == b:
    return friends_amount[a]

  if friends_amount[a] < friends_amount[b]:
    friends_amount[b] += friends_amount[a]
    network[a] = b
    return friends_amount[b]
  else:
    friends_amount[a] += friends_amount[b]
    network[b] = a
    return friends_amount[a]

if __name__ == "__main__":
  T = int(input())

  for _ in range(T):
    F = int(input())
    network = {}
    friends_amount = {}

    for _ in range(F):
      a, b = input().strip().split()

      if a not in network:
        network[a] = a
        friends_amount[a] = 1
      if b not in network:
        network[b] = b
        friends_amount[b] = 1

      print(union(network, friends_amount, a, b))
