"""
Imported randint from random
"""
from random import randint

# create hidden pattern and guess pattern with a range of 5
Hidden_Pattern = [[' ']*5 for x in range(5)]
Guess_Pattern = [[' ']*5 for x in range(5)]

alph_digit = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}


"""
create battleship board
"""


def create_board(board):
    print('# A B C D E')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


"""
generate ship locations
"""


def generate_ships():
    # user to enter row number between 1 and 5
    row = input('Enter a ship row 1 to 5 ').upper()
    while row not in '12345':
        print("Try enter a valid row ")
        row = input('Enter a ship row from 1 to 5 ')
    # user to enter column from A to E
    column = input('Enter a ship column from A to E ').upper()
    while column not in 'ABCDE':
        print("Try enter a valid column ")
        column = input('Enter a ship column from A to E ')
    return int(row)-1, alph_digit[column]