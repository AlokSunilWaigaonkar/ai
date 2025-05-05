def is_safe(board, col, row, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def nqueen(board, row, n):
    if row == n:
        print_solution(board, n)
        print()  # Separate different solutions
        return

    for col in range(n):
        if is_safe(board, col, row, n):
            board[row][col] = 1
            nqueen(board, row + 1, n)
            board[row][col] = 0  # Backtrack


def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] else '.', end=' ')
        print()


# Set N here
n = 5  # Change this to any N like 8 for 8-Queens
board = [[0 for _ in range(n)] for _ in range(n)]

print(f"All solutions for {n}-Queens:\n")
nqueen(board, 0, n)