import sys
sys.stdin = open("input.txt", "r")

# 시작 좌표에서 맨 앞으로 내려가는 함수
# return True : X 지점에 도달
# return False : X 지점에 도달하지 못함
def search_ladder(x, y):
    dxy = [[1, 0], [0,1], [0, -1]]
    # 지나온 곳만 체크할 수 있는 복사 배열을 하나 만들기
    # 이 친구는 바꿔도, 원본 배열에 영향 X
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1 # 초기 시작 위치는 이미 방문

    # 맨 밑에 도달할 때까지 계속 반복
    # 가장 마지막 줄에 도착할 때까지 반복
    while x != N - 1:
        # 3방향 델타 탐색
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] and not visited[nx][ny]:
                x, y = nx, ny
                visited[x][y] = 1

    return data[x][y] == 2

for _ in range(1, 11):
    test_case = int(input())
    N = 100
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    # 출발점 찾기
    # 출발점은 반드시 1행, 그리고 "1" 사다리에서만 출발 가능
    for j in range(N): # 열만 이동하면서 탐색
        if data[0][j] == 1: # 1행에서 "1" 사다리인 곳에서부터 탐색 시작
            if search_ladder(0, j):
                ans = j # True일 경우 X 지점을 찾았으니까 결과에 j를 대입
                break

    print(f"#{test_case} {ans}")
