import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    n, arr = input().split()
    n = int(n)

    while True:
        for idx in range(len(arr) - 1):
            if arr[idx] == arr[idx + 1]:
                arr = (arr[:idx] + arr[idx + 2:])
                break
        else:
            break

    print(f"#{test_case} {arr}")
