import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))

    ans = 0
    diff = []
    day = 1
    max_tree = max(trees) # 가장 큰 값 가져오기
    for tree in trees:
        diff.append(max_tree - tree)

    one = 0
    two = 0

    for i in range(len(diff)):
        if diff[i] == 0: # diff가 0이면 넘어감
            continue
        while diff[i] >= 1: # diff가 0이 될 때까지 빼줌
            if diff[i] % 2 == 1:
                one += 1
                diff[i] -= 1
            elif diff[i] % 2 == 0:
                two += 2
                diff[i] -= 2

    while one > 0 or two > 0:
        for i in range(len(trees)):
            if day % 2 == 1: # 홀수 날
                if one >= 1: # one이 1개라도 있다면 홀수 날에 -= 1
                    one -= 1
                    break
                else: # 홀수 날에 one이 하나도 없다면
                    if two == 2: # 2의 크기만 남았다면 1 - 1 보다 - 2가 더 빠르기 때문에 break
                        break
                    else: # 4 이상의 짝수 크기가 남았다면 1 2 1 2 1 2가 더 빠름
                        two -= 1
                        break
            else: # 짝수 날
                if two >= 2: # 2 이상의 크기가 남았다면 바로 빼줌
                    two -= 2
                    break

        day += 1
        ans += 1

    print(f"#{test_case} {ans}")
