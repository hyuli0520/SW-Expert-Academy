import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    R = [int(input()) for _ in range(n)]
    W = [int(input()) for _ in range(m)]
    tower = [int(input()) for _ in range(2 * m)]

    count_list = [0] * len(R)
    waiting_queue = deque() # 주차 대기 queue
    parking_list = list()
    count = 0
    ans = 0

    for i in range(len(tower)): # 총 8번 반복
        if tower[i] > 0:
            if len(parking_list) >= len(R): # 꽉 찼음
                waiting_queue.append(tower[i])
            else:
                # 주차 하기, [가장 작은 수의 주차장으로 들어가야함, 무게 넣어주기]
                for k in range(len(count_list)):
                    if count_list[k] == 0:
                        count = k
                        break
                parking_list.append([R[count], tower[i]])
                count_list[count] = tower[i]
        else:
            index = 0
            for idx in range(len(parking_list)):
                if abs(tower[i]) == parking_list[idx][1]:
                    index = idx
                    break

            items = parking_list.pop(index)
            ans += items[0] * W[items[1] - 1]

            for j in range(len(count_list)):
                if count_list[j] == abs(tower[i]):
                    count = j
            count_list[count] = 0

            if len(waiting_queue) > 0:
                for l in range(len(count_list)):
                    if count_list[l] == 0:
                        count = l
                        break
                waiting_car = waiting_queue.popleft()
                parking_list.append([R[count], waiting_car])
                count_list[count] = waiting_car

    print(f"#{test_case} {ans}")
