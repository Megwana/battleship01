"""
Imported randint from random
"""

from random import randint


HIDDEN_PATTERN = [[' ']*5 for x in range(5)]
GUESS_PATTERN = [[' ']*5 for x in range(5)]
"""Create hidden pattern and guess pattern with a range of 5"""

HIT_SYMBOL = '!'
MISS_SYMBOL = '~'

alph_digit = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}


def take_name_input():
    """Makes sure players name is 1 character or more"""
    try:
        user_name = input("Please enter your name: \n")
        if not user_name:
            raise Exception("Your First name must be greater than 1 character")
        return user_name
    except Exception as e:
        print(e)
        return take_name_input()


def welcome():
    """
    Opening message to the game that also takes in a name.
    """
    print("Welcome to Battleships")
    user_name = take_name_input()
    print(f"\nHi {user_name}! Welcome to Batteships!")
    print("""Your objective is to locate the enemy ships.
    \nThe coordinates are generated by the computer each time
    You will have to guess the coordinates of the enemy ships.
    \nOne hit equals one sunken ship on the enemy\'s board.
    \n'!' symbolises and explosion, meaning they are hit targets.
    \n'~' symbolises open water, meaning the shot has missed the enemy ship.
    \nBe aware that the grid is five wide, using integers 1-5 and Letters A-E.
    """)


def create_board(board):
    """
    create battleship board
    """
    print('# A B C D E')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def generate_ships():
    """
    Generate ship locations on the battleship board.
    Ensuring its 1 to 5 and A to E.
    """
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


def random_ships(board):
    """
    function creates random ship locations on board.
    Using the randint imported at the begining.
    """
    for ship in range(5):
        ship_row, ship_col = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_col] == HIT_SYMBOL:
            ship_row, ship_col = randint(0, 4), randint(0, 4)
        board[ship_row][ship_col] = HIT_SYMBOL


def count_sunk_ships(board):
    """
    function for the game to keep a track of how many ships have been hit.
    And to increment count by 1 each time '!' is registered.
    """
    count = 0
    for row in board:
        for column in row:
            if column == HIT_SYMBOL:
                count += 1
    return count


def main():
    """Define the main game loop with introduction message"""
    welcome()
    random_ships(HIDDEN_PATTERN)
    # generate the ships function with the hidden pattern.
    turns = 20
    # player has 20 turns to guess the location of the three ships.
    board_pattern = GUESS_PATTERN
    while turns > 0:
        print("\nEnemy Battleship Board")
        create_board(board_pattern)
        row, column = generate_ships()
        if board_pattern[row][column] == MISS_SYMBOL:
            print("You have already guessed these coordinates, try again")
        elif board_pattern[row][column] == HIT_SYMBOL:
            print("Congratulations! \
                You have hit and sank an enemy battleship.")
            board_pattern[row][column] = HIT_SYMBOL
            # deduct a turn each time.
            turns -= 1
        else:
            print("Unlucky soldier, you missed the target.")
            board_pattern[row][column] = MISS_SYMBOL
            turns -= 1
        if count_sunk_ships(board_pattern) == 3:
            # player needs to locate 3 ships to win.
            print("""Congratulations! Mission complete
            \n All enemy ships have been hit.""")
            exit()
        print(' You have ' + str(turns) + ' turns remaining ')
        if turns == 0:
            game_over_input = input('Game Over, \
                press enter to exit the game\n')


main()
