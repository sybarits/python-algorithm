def solution(board, nums):
    answer = 0
    board_size = len(board)
    nums = set(nums)
    row_count = [0 for _ in range(board_size)]
    col_count = [0 for _ in range(board_size)]

    #대각선 정방향
    diag_count_1 = 0
    # 대각선 역방향
    diag_count_2 = 0

    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] in nums:
                row_count[i] += 1
                col_count[j] += 1
                if i == j:
                    diag_count_1 += 1
                if board_size - 1 - i == j:
                    diag_count_2 += 1

    for i in range(board_size):
        if row_count[i] == board_size:
            answer += 1
        if col_count[i] == board_size:
            answer += 1
    if diag_count_1 == board_size:
        answer += 1
    if diag_count_2 == board_size:
        answer += 1    
    
    print("answer",answer)
    return answer


if __name__ == "__main__":
    solution([[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]], [14,3,2,4,13,1,16,11,5,15])
    # solution([[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]], [15,7,2,25,9,16,12,18,5,4,10,13,20])