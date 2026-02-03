import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N = 열, M = 행
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]  # 상, 하, 좌, 우
    dy = [1, -1, 0, 0]  # 상, 하, 좌, 우

    ans = 0
    for i in range(N):
        for j in range(M): # 행 -> 열 순으로 확인
            tmp = matrix[i][j] # matrix의 i, j 번째에 있는 수를 tmp에 저장

            high = matrix[i][j]
            for dist in range(1, tmp + 1):
                for k in range(4): # (i, j)를 기준으로 상, 하, 좌, 우를 dist 만큼 탐색
                    ni = i + (dx[k] * dist)
                    nj = j + (dy[k] * dist)

                    if 0 <= ni < N and 0 <= nj < M:
                        high += matrix[ni][nj]

            if ans < high:
                ans = high

    print(f"#{test_case} {ans}")
