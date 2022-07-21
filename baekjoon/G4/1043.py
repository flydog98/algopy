# 1043번 거짓말

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find(people, person_no):
  if person_no == people[person_no]:
    return person_no

  people[person_no] = find(people, people[person_no])
  return people[person_no]

def union(people, truth, a, b):
  a = find(people, a)
  b = find(people, b)

  if a == b:
    return
  
  if truth[b] == 1:
    people[a] = b
  else:
    people[b] = a

def process(people, truth, party_input):
  for i in range(1, len(party_input)):
    union(people, truth, party_input[0], party_input[i])

if __name__ == "__main__":
  answer = 0
  N, M = map(int, input().split())

  truth_input = list(map(int, input().strip().split()))
  truth = [0 for x in range(N + 1)]
  for i in range(1, len(truth_input)):
    truth[truth_input[i]] = 1

  people = [x for x in range(N + 1)]
  party_store = []

  for _ in range(M):
    party_input = list(map(int, input().strip().split()))

    process(people, truth, party_input[1:])
    party_store.append(party_input[1:])

  for party in party_store:
    flag = True
    for person_no in party:
      if truth[find(people, person_no)] == 1:
        flag = False
    if flag:
      answer += 1

  print(answer)
