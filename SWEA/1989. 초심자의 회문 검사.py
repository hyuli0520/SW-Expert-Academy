import sys
sys.stdin = open("input.txt", "r")

def is_palindrome(word, left, right):
    if left >= right:
        return 1

    if word[left] != word[right]:
        return 0

    return is_palindrome(word, left + 1, right - 1)

T = int(input())

for test_case in range(1, T + 1):
    word = input().strip()
    word_len = len(word)

    result = is_palindrome(word, 0, word_len - 1)

    print(f"#{test_case} {result}")
