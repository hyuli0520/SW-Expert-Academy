import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    correct_sheet = list(map(int, input().split()))
    # 학생들이 입력한 시험지
    students_sheet = [list(map(int, input().split())) for _ in range(N)]

    # 학생들의 점수 중 최고점 - 최저점
    max_score = 0
    min_score = float("inf")

    for student_sheet in students_sheet:
        # 학생들의 점수
        student_score = 0 # 정답을 맞힐 때마다 점수 누적
        correct_count = 0 # 연속해서 맞춘 개수, 틀리면 초기화

        for i in range(M):
            if student_sheet[i] == correct_sheet[i]:
                correct_count += 1
                student_score += correct_count
            else:
                correct_count = 0

        max_score = max(max_score, student_score)
        min_score = min(min_score, student_score)

    ans = max_score - min_score
    print(f"#{test_case} {ans}")
