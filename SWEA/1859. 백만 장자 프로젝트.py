import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def get_max_index(sale, N, next):
    # 뒤에서부터 확인하여 최대 index 찾기
    max_price = -1
    max_index = 0
    for idx in range(N - 1, next - 1, -1):
        if max_price < sale[idx]:
            max_index = idx
            max_price = sale[idx]

    return max_index


for test_case in range(1, T + 1):
    N = int(input())
    sale_price = list(map(int, input().split()))

    ans = 0

    count = 0 # 현재 끝난 후 max_index 값을 넣어 끝나야하는지 확인하는 함수
    end = 0 # 현재 값 차이 매꾸기
    max_idx = 0 # 최대 값의 인덱스
    while count < N - 1: # 이전 max_index 값이 끝에 있다면 while문 끝내기
        max_idx = get_max_index(sale_price, N, count + end)
        if max_idx == 0:
            break

        buy_price = 0 # 얼마 더하는지 세기
        add_count = 0 # 몇번 더했는지 세기
        for i in range(count + end, max_idx):
            buy_price += sale_price[i]
            add_count += 1

        ans += (sale_price[max_idx] * add_count) - buy_price # 최대 가격 * 개수 - 산 가격

        if max_idx == N - 1:
            end = 0
        else:
            end = 1
        count = max_idx

    print(f"#{test_case} {ans}")
