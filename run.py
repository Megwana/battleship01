"""
Imported randint from random
"""
from random import randint


HIDDEN_PATTERN = [[' '] * 5 for x in range(5)]
GUESS_PATTERN = [[' '] * 5 for x in range(5)]
"""Create hidden pattern and guess pattern with a range of 5"""

# Constants that are used to represent what is on the board
HIT_SYMBOL = '!'
MISS_SYMBOL = '~'

alph_digit = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}


def take_name_input():
    """
    Makes sure player's name is 1 character or more
    """
    while True:
        try:
            user_name = input("Please enter your name: \n")
            if not user_name:
                raise ValueError("Your first name must be at least"
                                 + " 1 character")
            if any(char.isdigit() for char in user_name):
                raise ValueError("Your first name must contain only letters")
            return user_name
        except ValueError as e:
            print(e)


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
    \nIf you hit 3 ships, you will win the game.
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
        print(f"{row_num}|{'|'.join(row)}|")
        row_num += 1


def generate_ships():
    """
    Generate ship locations on the battleship board.
    Ensuring its 1 to 5 and A to E.
    """
    # User to enter row number between 1 and 5
    while True:
        try:
            row = input("Enter row (1-5): ")
            if row.isdigit() and 1 <= int(row) <= 5:
                row = int(row) - 1
                break
            else:
                # Raise an error if blank or invalid number is entered
                raise ValueError(
                    "Invalid input. Please enter a number between 1 and 5.")
        except ValueError as e:
            print(e)
            print("Please try again.")

    while True:
        try:
            column = input("Enter column (A-E): ")
            if (column.isalpha() and len(column) == 1
                    and 'A' <= column.upper() <= 'E'):
                column = alph_digit[column.upper()]
                break
            else:
                # Raise an error if blank or invalid letter is entered
                raise ValueError(
                    "Invalid input. Please enter a letter between A and E.")
        except ValueError as e:
            print(e)
            print("Please try again.")
    return row, column


def random_ships(board):
    """
    function creates random ship locations on board.
    Using the randint imported at the begining.
    """
    for _ in range(5):
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
    """
    Define the main game loop with introduction message
    """
    welcome()
    random_ships(HIDDEN_PATTERN)
    # Generate the ships function with the hidden pattern.
    turns = 20
    # Player has 5 turns to guess the location of the three ships.
    board_pattern = GUESS_PATTERN
    while turns > 0:
        print("\nEnemy Battleship Board")
        create_board(board_pattern)
        row, column = generate_ships()
        # Checks whether the coordinates have already been used on a turn
        if board_pattern[row][column] == MISS_SYMBOL:
            print("You have already guessed these coordinates, try again")
        # Lets user know they have hit an enemy ship
        elif board_pattern[row][column] == HIT_SYMBOL:
            print("Congratulations!"
                  + "You have hit and sank an enemy battleship.")
            board_pattern[row][column] = HIT_SYMBOL
            # Deduct a turn each hit
            turns -= 1
        else:
            # Lets the user know they have missed the target
            print("Unlucky soldier, you missed the target.")
            board_pattern[row][column] = MISS_SYMBOL
            # Deduct a turn each miss
            turns -= 1
        print(' You have ' + str(turns) + ' turns remaining ')
    # Player needs to locate 3 ships to win.
    if count_sunk_ships(board_pattern) == 3:
        print("""Congratulations! Mission complete
        \n All enemy ships have been hit.""")
        exit()
    while turns == 0:
        play_input = input(
            "Do you want to play again? (Y/N): ").strip().lower()
        if play_input == 'y':
            main()
            break
        elif play_input == 'n':
            print("Goodbye for now!")
            quit()
        else:
            print("Please enter 'Y' or 'N'")


main()
