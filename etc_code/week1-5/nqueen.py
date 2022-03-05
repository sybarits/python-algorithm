def solution(n):
    board = [0] * (n + 1)
    return nqueen(board,n,0)


def nqueen(queen, n, row):
    count = 0
    
    if n == row:
        return 1
    
    for col in range(n):
        queen[row] = col
        if isGood(row,queen):
            count += nqueen(queen, n, row+1)
            
    return count

def isGood (j, board):
    for i in range(j):
        if (board[j] == board[i] or abs(board[j] - board[i]) == (j - i)):
            return False
    return True

if __name__ == "__main__":
    print(solution(4))
    print(solution(5))