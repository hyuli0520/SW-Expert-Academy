import sys
sys.stdin = open("input.txt", "r")

size = 9
def check_sudoku(sudoku):
    for i in range(size):
        x_list = []
        y_list = []
        for j in range(size):
            x_list.append(sudoku[i][j]) # 행에 있는 수 전부 넣기
            y_list.append(sudoku[j][i]) # 열에 있는 수 전부 넣기

        x_list.sort() # 행에 있는 수 정렬
        y_list.sort() # 열에 있는 수 정렬

        x_count = 0
        y_count = 0
        for idx in range(1, size + 1): # 행과 열 안에 1~9까지 확인 만약 하나라도 없으면 실패 -> return 0
            if x_list[idx - 1] == idx:
                x_count += 1
            if y_list[idx - 1] == idx:
                y_count += 1

        if x_count != 9:
            return 0
        if y_count != 9:
            return 0

    return 1

def sq_sudoku(sudoku):
    for i in range(0, 9, 3): # 네모 열 확인      [] [] []
        for j in range(0, 9, 3): # 네모 행 확인  [] [] []
            sq_list = [] #                      [] [] []
            for k in range(3): # 네모 안에 있는 수 확인
                for l in range(3): # 네모 안에 있는 수 확인
                    sq_list.append(sudoku[k][l])

            sq_list.sort() # 네모 안에 있는 수 정렬

            sq_count = 0
            for idx in range(1, size + 1): # 3x3 네모 안에 1~9까지 확인 만약 하나라도 없으면 실패 -> return 0
                if sq_list[idx - 1] == idx:
                    sq_count += 1

            if sq_count != 9:
                return 0

    return 1


T = int(input())

for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(size)]
    ch = check_sudoku(sudoku) # sudoku 가로 세로 확인하기
    sq = sq_sudoku(sudoku) # sudoku 3x3 네모 확인하기

    ans = 0
    if ch and sq:
        ans = 1

    print(f"#{test_case} {ans}")
