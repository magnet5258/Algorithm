def isValid(arr):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1
    return True


def solution():
    # 최소 길이 : 1
    length = 1

    # 행 탐색
    for row in range(L):
        now_maxLen = length
        for col in range(L - length):
            for search_len in range(length + 1, L - col + 1):
                if board[row][col] == board[row][col + search_len - 1]:
                    temp = board[row][col: col + search_len]
                    if isValid(temp):
                        now_maxLen = search_len
            length = max(length, now_maxLen)
        # length가 최대 값이라면 함수 종료
        if length == L:
            return length

    # 열 탐색
    for col in range(L):
        now_maxLen = length
        for row in range(L - length):
            for search_len in range(length + 1, L - row + 1):
                if board[row][col] == board[row + search_len - 1][col]:
                    temp = []
                    for _row in range(row, search_len + row):
                        temp.append(board[_row][col])
                    if isValid(temp):
                        now_maxLen = search_len
            length = max(length, now_maxLen)
        if length == L:
            return length
    
    return length

T = 10

for _ in range(T):
    test_case = int(input())
    L = 100
    board = []
    for _ in range(L):
        board.append(input())
    
    
    print(f'#{test_case} {solution()}')