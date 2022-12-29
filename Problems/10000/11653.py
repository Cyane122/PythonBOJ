"""
BOJ 11653 소인수분해 - https://www.acmicpc.net/problem/11653
Tier: Bronze I
"""

a = int(input())
i = 2
while True:
    if a % i == 0:
        a = a/i
        print(i)
    else:
        i += 1
    if a == 1:
        break
