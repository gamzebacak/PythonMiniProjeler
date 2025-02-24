import random
from prettytable import PrettyTable


def print_board(board):
    table = PrettyTable()
    for row in board:
        table.add_row([str(num) if num != 0 else '.' for num in row])
    print(table)


def is_valid(board, num, pos):
    row, col = pos

    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False

    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0

    return False


def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid(board, num, (row, col)) or board[row][col] != 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num
    return board


def play_sudoku():
    board = generate_board()
    while True:
        print_board(board)
        try:
            row = int(input("Satır (1-9): ")) - 1
            col = int(input("Sütun (1-9): ")) - 1
            num = int(input("Sayı (1-9): "))

            if board[row][col] == 0 and is_valid(board, num, (row, col)):
                board[row][col] = num
            else:
                print("Geçersiz hamle, tekrar deneyin.")

            if find_empty(board) is None:
                print("Tebrikler, Sudoku'yu çözdünüz!")
                break
        except (ValueError, IndexError):
            print("Lütfen geçerli bir giriş yapın.")


if __name__ == "__main__":
    play_sudoku()
