import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    high = -1
    for i in range(N - M + 1): # N - M + 1 out of lange가 안 나게끔 설정 후, 배열을 쭉 돌기
        for j in range(N - M + 1): # 위와 동일
            total = 0
            for k in range(M): # M의 크기만큼 확인 필요
                for m in range(M): # M의 크기만큼 확인 필요
                    total += flies[k+i][m+j]

            if high < total:
                high = total

    print(f"#{test_case} {high}")
