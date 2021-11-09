# 17219번 비밀번호 찾기

import sys

N, M = map(int, sys.stdin.readline().split())

site_dict = {}

for _ in range(N):
  site, secret = sys.stdin.readline().split()
  site_dict[site] = secret
  
for _ in range(M):
  site = sys.stdin.readline().rstrip()
  print(site_dict[site])
