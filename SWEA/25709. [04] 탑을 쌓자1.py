import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, t1_h, t2_h = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    weights.sort(reverse=True)

    total = 0
    count_t1_h = 1 # tower1에서 화물을 놓아야하는 위치
    count_t2_h = 1 # tower2에서 화물을 놓아야하는 위치

    for i in range(n):
        if count_t1_h > t1_h:
            total += (count_t2_h * weights[i])
            count_t2_h += 1
        elif count_t2_h > t2_h:
            total += (count_t1_h * weights[i])
            count_t1_h += 1
        elif count_t1_h <= count_t2_h:
            total += (count_t1_h * weights[i])
            count_t1_h += 1
        elif count_t1_h > count_t2_h:
            total += (count_t2_h * weights[i])
            count_t2_h += 1

    print(f"#{test_case} {total}")
