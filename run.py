from random import randint

# create hidden pattern and guess pattern with a range of 5
Hidden_Pattern = [[' ']*5 for x in range(5)]
Guess_Pattern = [[' ']*5 for x in range(5)]

alph_digit = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}


# create battleship board
def print_board(board):
    print('# A B C D E')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1