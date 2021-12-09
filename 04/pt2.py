import csv, re

def main():

    try:
        with open("./input") as f:
            numbers, boards = parse_input(f)
            winning_boards = []
            for number in numbers:
                for board_index, board in enumerate(boards):
                    if board is None:
                        continue
                    for line in board:
                        for index, line_number in enumerate(line):
                            if line_number == number:
                                line[index] = None
                                if is_winning_board(board):
                                    winning_boards.append([board, number])
                                    boards[board_index] = None

            print(calc_winning_score(winning_boards[len(winning_boards)-1][0], winning_boards[len(winning_boards)-1][1]))

    finally:
        f.close()

def calc_winning_score(board, number):
    total = 0
    for line in board:
        for line_number in line:
            if line_number != None:
                total += int(line_number)
    return total * int(number)

def is_winning_board(board):
    for line in board:
        winning_line = True
        for line_number in line:
            if line_number != None:
                winning_line = False
        if winning_line:
            return True

    for i, val in enumerate(board[0]):
        winning_col = True
        for line in board:
            if line[i] != None:
                winning_col = False
        if winning_col:
            return True
    return False

def parse_input(f):
    reader = csv.reader(f)
    numbers = [int(x) for x in next(reader)]
    next(reader)
    boards = []
    board = []
    for line in reader:
        if line == []:
            boards.append(board)
            board = []
        else:
            split_line = [int(x) for x in re.split("\s{1,2}", line[0].strip())]
            board.append(split_line)
    boards.append(board)
    return numbers, boards

if __name__ == "__main__":
    main()