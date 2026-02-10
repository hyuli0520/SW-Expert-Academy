import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
start = [0] # 가장 높은 곳이 어디서 시작하는지
high_count = 0 # 가장 높은 곳이 몇개나 있는지
for test_case in range(1, T + 1):
    N = int(input())
    high_map = [list(map(int, input().split())) for _ in range(N)]

    temp_high = -1 # 가장 높은 곳을 확인하는 임시변수
    for i in range(N):
        for j in range(N):
            if high_map[i][j] > temp_high:
                temp_high = high_map[i][j] # 가장 높은 곳 대입
                start.clear()
                start.append([i, j])
            elif high_map[i][j] == temp_high:
                start.append([i, j])

    max_ans = 1
    for _ in range(len(start)):
        ans = 1
        start_y, start_x = start.pop()
        ny, nx = 0, 0
        min_y, min_x = 0, 0
        break_for = False
        while True:
            low = 99999
            low_index = 0
            for i in range(4):
                ny = dy[i] + start_y
                nx = dx[i] + start_x

                if 0 <= ny < N and 0 <= nx < N:
                    if low > high_map[ny][nx]:
                        low = high_map[ny][nx]
                        min_y, min_x = ny, nx

            if low < high_map[start_y][start_x]:
                start_y, start_x = min_y, min_x
                ans += 1
            else:
                break

        if ans > max_ans:
            max_ans = ans

    print(f"#{test_case} {max_ans}")
