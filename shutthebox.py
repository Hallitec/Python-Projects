from random import randint
import time

# Initializing variables
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
score = 0
game_running = True
dice_one = ''
dice_two = ''
total_dice = ''

# Randomly generates two dice rolls 1 - 6
# Converts int to str and prints the dice rolls to the screen
def throw_dice():
    global dice_one, dice_two, total_dice, score
    roll_one, roll_two = randint(1,6), randint(1,6)
    score += 1
    total_roll = roll_one + roll_two
    dice_one = str(roll_one)
    dice_two = str(roll_two)
    total_dice = str(total_roll)
    dice_art = """\n
    First roll        Second roll                           
    |=|=|=|=|=|       |=|=|=|=|=|
    |=|=====|=|       |=|=====|=|
    |=|  a  |=|       |=|  b  |=|
    |=|=====|=|       |=|=====|=|                    
    |=|=|=|=|=|       |=|=|=|=|=|
    """
    print('\n___ Players turn ___'
    '\n\nThrowing dice!'
    '\nCalculating...')
    time.sleep(2)
    print(dice_art
        .replace('a', (dice_one))
        .replace('b', (dice_two)))
    print('\nDice one:', dice_one,' Dice two:', dice_two,' Total dice:', total_dice)


# Prints the tiles remaining after each turn
def output_board():
    print('\nTiles remaining:', board)

# Uses a for loop to iterate through each character in a players input.
# If character not on the board it prints a response.
# If character is on board it removes from board and prints a confirmation.
def update_board():
    for n in player_move:
        if n not in board:
            print(n, 'is not on the board.')
        if n in board:
            board.remove(n)
            print(n, 'has been removed from the board.')

# Returns False for each invalid input
def validate_moves():
    for n in player_move:
        if n not in [dice_one, dice_two, total_dice]:
            print('\nThat is not a valid move. Please try again.')
            return False
        if dice_one in player_move and total_dice in player_move:
            print('Dice 1 and total cant be used together.')
            return False
        if dice_two in player_move and total_dice in player_move:
            print('Dice 2 and total cant be used together')
            return False
    return True

        
# Closing credits when player exits the game.
def closing_credits():
    global game_running
    print("""
    \n\n=== 'Shut The Box' Credits ===
    \nDeveloped by: Matt Halliday
    \nAll Rights Reserved.
    \n==============================
    \nThanks for playing!
    """)
    game_running = False


# Main menu function that calls a function based on the user input.
# If the input is invalid it returns the player to the main menu options.
def main_menu():
    global game_running
    print("\n|=|=| Welcome to 'Shut The Box' |=|=|")
    option_chosen = str(input("\nPlay the game [P]"
                            "\nRead the rules [R]"
                            "\nQuit the game [Q]"
                            "\n\nWhat would you like to do? ")).upper()
    if option_chosen.startswith('P'):
        game_running = True
    elif option_chosen.startswith('R'):
        print("""\n
        =======   'Shut The Box' Game Rules   =======
        You can use the dice rolls separately to eliminate tiles.
        You can use the combined total of the dice to eliminate a tile.
        Eliminate all tiles in the fewest amount of moves.
        """)
        main_menu()
    elif option_chosen.startswith('Q'):
        closing_credits()
    else:
        print('\nChoose from one of the options in the menu.')
        main_menu()

# Game starts from the main menu function being called below.
main_menu()

# Main game code that calls different functions based on user input
while game_running == True:
        throw_dice()
        output_board()
        player_move = str(input('\n\nEnter numbers you want to use separated by a space'
        '\nOr Press [q] to exit the game'
        '\nOr press enter if there is no move: ')).lower()
        if player_move == 'q':
            closing_credits()
            break
        player_move = player_move.split()
        if validate_moves():
            update_board()
        if board == []:
            print('\n\nYou removed all tiles from the board in: ', score,'moves.\n\nCongratulations !')
            time.sleep(1)
            closing_credits()





        

        


