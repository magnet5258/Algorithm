def is_palindrome(string, start, end):
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

def find_longest_palindrome(grid, size):
    max_length = 1

    # 가로 방향 회문 탐색
    for row in range(size):
        for start in range(size):
            for end in range(size - 1, start + max_length - 1, -1):
                if is_palindrome(grid[row], start, end):
                    max_length = max(max_length, end - start + 1)
                    break

    # 세로 방향 회문 탐색
    for col in range(size):
        for start in range(size):
            for end in range(size - 1, start + max_length - 1, -1):
                column_string = [grid[row][col] for row in range(start, end + 1)]
                if is_palindrome(column_string, 0, end - start):
                    max_length = max(max_length, end - start + 1)
                    break

    return max_length

# 테스트 케이스 실행
T = 10
N = 100  # 글자판의 크기

for _ in range(T):
    test_case = int(input())  # 테스트 케이스 번호
    board = [input().strip() for _ in range(N)]  # 글자판 입력
    result = find_longest_palindrome(board, N)
    print(f'#{test_case} {result}')