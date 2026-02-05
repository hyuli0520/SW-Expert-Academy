import sys
sys.stdin = open("input.txt", "r")

T = int(input())

matching_dict = {
    'p': 'q',
    'q': 'p',
    'b': 'd',
    'd': 'b'
}

for test_case in range(1, T + 1):
    str_input = input().strip() # 한 글자씩 리스트에 input

    list_to_str = ""
    for i in range(len(str_input) - 1, -1, -1): # 뒤에서부터 넣어주기
        if str_input[i] in matching_dict.keys():
            list_to_str += matching_dict[str_input[i]] # 뒤집은 후 string에 input

    print(f"#{test_case} {list_to_str}")
