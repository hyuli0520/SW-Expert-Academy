import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [[0, 1], [1, 1], [1, 0], [1, -1]]

for test_case in range(1, T + 1):
    N = int(input())
    gomoku = [list(map(str, input().strip())) for _ in range(N)]

    ans = "NO"
    for i in range(N):
        for j in range(N):
            for dy, dx in dxy:
                if gomoku[i][j] == 'o':
                    nx = j
                    ny = i
                    count = 1
                    for k in range(1, 6):
                        nx += dx
                        ny += dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if gomoku[ny][nx] == 'o':
                                count += 1
                            else:
                                break

                    if count >= 5:
                        ans = "YES"

    print(f"#{test_case} {ans}")
