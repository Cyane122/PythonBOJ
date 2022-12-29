"""
BOJ 1978 소인수분해 - https://www.acmicpc.net/problem/1978
Tier: Silver V
"""

N = int(input())
R = 0
li = list(input().split())

for i in li:
    k = int(i)
    if k == 1:
        R = R+1
        continue
    for j in range(2, k-1):
        if k % j == 0 and k != j:
            R = R + 1
            break
print(N - R)
