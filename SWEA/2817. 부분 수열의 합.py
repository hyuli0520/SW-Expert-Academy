import sys
sys.stdin = open("input.txt", "r")
from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    comb_list = list(map(int, input().split()))

    ans = 0
    for i in range(1, N + 1):
        for comb in combinations(comb_list, i):
            if sum(comb) == K:
                ans += 1

    print(f"#{test_case} {ans}")
