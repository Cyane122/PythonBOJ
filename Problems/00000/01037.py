# BOJ 1037 약수 - https://www.acmicpc.net/problem/1037
# Tier: Bronze I

N = int(input())
L = list(map(int, input().split()))

print(max(L) * min(L))

