import sys
sys.stdin = open("input.txt", "r")
from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    min_diff = float('inf')
    ingredients = list(range(N))
    
    # 모든 N/2 조합 생성
    comb = list(combinations(ingredients, N // 2))
    
    # 대칭 제거 후 절반만 탐색
    for i in range(len(comb) // 2):
        cook_a = comb[i]
        cook_b = set(ingredients) - set(cook_a)
        
        sum_a = 0
        sum_b = 0
        
        # cook_b 요리
        for i, j in combinations(cook_a, 2):
            sum_a += S[i][j] + S[j][i]
        
        # cook_a 요리
        for i, j in combinations(cook_b, 2):
            sum_b += S[i][j] + S[j][i]
        
        min_diff = min(min_diff, abs(sum_a - sum_b))
    
    print(f"#{test_case} {min_diff}")
