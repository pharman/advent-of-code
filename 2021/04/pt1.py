import csv, re

def main():
    cnt = 0

    try:
        with open("input") as f:
            numbers, boards = parse_input(f)
            for number in numbers:
                for board in boards:
                    for line in board:
                        for index, line_number in enumerate(line):
                            if line_number == number:
                                line[index] = None
                                if is_winning_board(board):
                                    score = calc_winning_score(board, number)
                                    print(score)
                                    exit()


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

    for i in range(len(board[0])):
        winning_col = True
        for line in board:
            if line[i] != None:
                winning_col = False
    return winning_col

def parse_input(f):
    reader = csv.reader(f)
    numbers = next(reader)
    next(reader)
    boards = []
    board = []
    for line in reader:
        if line == []:
            boards.append(board)
            board = []
        else:
            board.append(re.split("\s{1,2}", line[0].strip()))
    return numbers, boards

if __name__ == "__main__":
    main()