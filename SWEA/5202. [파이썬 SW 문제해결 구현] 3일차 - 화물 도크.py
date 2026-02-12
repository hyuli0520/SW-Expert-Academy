import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    input_map = [tuple(map(int, input().split())) for _ in range(N)]
    input_map.sort(key=lambda x: x[1])

    count = 0
    now = 0
    for start, end in input_map:
        if now > start:
            continue

        now = end
        count += 1

    print(f"#{test_case} {count}")
