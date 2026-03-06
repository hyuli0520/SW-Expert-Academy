T = int(input())

# 현재 위치에 퀸을 놓을 수 있는지 검사하는 함수
def is_vaild_pos(board, row, col):
    # 현재 옆에 있는지 검사
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    # 왼쪽 윗 대각선
    for i, j in zip(range(row -1, -1, -1), range(col -1, -1, -1)):
        if board[i][j] == 1:
            return False

    # 오른쪽 윗 대각선
    for i, j in zip(range(row -1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False
        
    return True

# row: 현재 퀸을 놓을 행
# board: 퀸들의 위치를 나타내는 n * n 보드
def n_queens(board, row):
    global ans
    if row == n:
        ans += 1
        return
    
    # row는 퀸을 놓을 행
    # 행은 고정
    for col in range(n):
        if is_vaild_pos(board, row, col): # 퀸을 row, col에 놓을 자격이 있는지 확인 후, 재귀호출
            board[row][col] = 1 # row, col에 퀸을 놓는다
            n_queens(board, row + 1)
            board[row][col] = 0 # 되돌리기

for test_case in range(1, T + 1):
    n = int(input())
    board = [[0] * n for _ in range(n)] # n * n 2차원 배열 생성in
    ans = 0

    n_queens(board, 0)

    print(f"#{test_case} {ans}")
