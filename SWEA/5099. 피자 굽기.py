import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    cheeses = list(map(int, input().split()))

    fire_queue = deque()
    for i in range(N):
        fire_queue.append([i, cheeses[i]])

    waiting_queue = deque()
    for i in range(N, M):
        waiting_queue.append([i, cheeses[i]])

    # 화덕에서 피자가 하나 남을 때까지, 피자 꺼내서 확인하고, 집어넣는 로직 반복
    while len(fire_queue) > 1:
        pizza = fire_queue.popleft() # 피자 꺼내기
        pizza[1] //= 2

        if pizza[1]: # 피자의 양이 0이 아니면, 다시 화덕에 넣음
            fire_queue.append(pizza)
            continue

        # 꺼낸 피자의 양이 0이 돼서 화덕이 한칸 비면
        # 대기하고 있는 피자 넣기
        if waiting_queue and len(fire_queue) != N:
            fire_queue.append(waiting_queue.popleft()) # 대기 피자를 꺼내서 집어넣는다

    print(f"#{test_case} {fire_queue[0][0] + 1}")
