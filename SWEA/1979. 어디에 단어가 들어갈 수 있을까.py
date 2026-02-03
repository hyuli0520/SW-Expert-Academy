import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        white_count = 0
        for j in range(N): # 행 순회
            if matrix[i][j] == 1:
                white_count += 1
            elif matrix[i][j] == 0:
                white_count = 0

            if white_count == K:
                if j >= N - 1:
                    ans += 1
                else:
                    if matrix[i][j + 1] == 0:
                        ans += 1

        white_count = 0
        for k in range(N): # 행 순회
            if matrix[k][i] == 1:
                white_count += 1
            elif matrix[k][i] == 0:
                white_count = 0

            if white_count == K:
                if k >= N - 1:
                    ans += 1
                else:
                    if matrix[k + 1][i] == 0:
                        ans += 1

    print(f"#{test_case} {ans}")
