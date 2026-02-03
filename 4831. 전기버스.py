import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    battery = list(map(int, input().split()))

    now_pos = 0
    count = 0
    ans = 0
    break_while = False
    while N != now_pos:
        break_for = False
        for i in range(K + now_pos, now_pos, -1):
            now_pos = i
            if now_pos == N:
                break

            count += 1
            if count > K:
                ans = 0
                break_while = True
                break

            for j in range(len(battery)):
                if battery[j] == now_pos:
                    ans += 1
                    count = 0
                    break_for = True
                    break

            if break_for == True:
                break

        if break_while == True:
            break

    print(f"#{test_case} {ans}")
