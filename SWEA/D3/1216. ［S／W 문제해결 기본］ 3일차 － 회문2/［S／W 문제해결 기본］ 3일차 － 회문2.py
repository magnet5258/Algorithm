def isPalindrome(string, start, end):
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


def findLongestPalindrome(board, L):
    max_length = 1

    # 행 탐색
    for row in range(L):
        for start in range(L):
            for end in range(L - 1, start + max_length - 1, -1):
                if isPalindrome(board[row], start, end):
                    max_length = max(max_length, end - start + 1)
                    break

    # 열 탐색
    for col in range(L):
        for start in range(L):
            for end in range(L - 1, start + max_length - 1, -1):
                column_string = [board[row][col] for row in range(start, end + 1)]
                if isPalindrome(column_string, 0, end - start):
                    max_length = max(max_length, end - start + 1)
                    break

    return max_length


T = 10
L = 100

for _ in range(T):
    test_case = int(input())
    board = [input() for _ in range(L)]
    result = findLongestPalindrome(board, L)
    print(f'#{test_case} {result}')
