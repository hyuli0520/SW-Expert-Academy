import sys
sys.stdin = open("input.txt", "r")

T = int(input())


# 활주로 한 줄 확인하기
def check_runway(runways, n, x):
    visited = [False] * n
    result = 0
    for idx in range(n - 1):
        now = runways[idx]
        nxt = runways[idx + 1]

        if abs(nxt - now) > 1: # 만약 next에서 now를 뺐을 때 1이 넘어가면(높이가 2이상 차이나면) break
            break
        elif nxt - now == 1: # 한칸 위로 올라갈 때
            count = 0
            for j in range(idx, -1, -1):
                if visited[j]:
                    return 0
                count += 1
                if count < x:
                    visited[j] = True
                    if runways[j] == now:
                        continue
                    else:
                        count = 0
                else:
                    count = 0
                    break
            else:
                break
        elif nxt - now == -1: # 한칸 아래로 내려갈 때
            down = 0
            while down < x:
                down += 1
                if down >= x:
                    visited[idx + down] = True
                    continue
                if idx + down >= N - 1:
                    break
                elif runways[idx + down] == runways[idx + down + 1]:
                    visited[idx + down] = True
                    continue
                else:
                    break
            else:
                continue

            break
    else:
        result += 1

    return result


for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    lists = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        ans += check_runway(lists[i], N, X)

    arr = list(map(list, zip(*lists[::-1])))
    for k in range(N):
        ans += check_runway(arr[k], N, X)

    print(f"#{test_case} {ans}")
