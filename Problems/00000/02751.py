"""
BOJ 2751 수 정렬하기 - https://www.acmicpc.net/problem/2751
Tier: Silver V
"""

N = int(input())
L = list(map(int, input().split()))

for i in range(N):
    L.append(int(input()))

L = sorted(set(L))

for i in L:
    print(i)