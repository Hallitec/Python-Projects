import random

# Defining game rules.
welcome_msg = ('welcome to the ultimate'
               '[rock, paper, scissors]'
               'game of the century!')
rules = ('\nThe rules are simple...'
         '\n\nRock beats scissors.'
         '\nPaper beats rock.'
         '\nScissors beats paper.')
# Printing uppercase strings.        
print(welcome_msg.upper()) 
print(rules.upper())      

# Set default values.
player_score = 0
computer_score = 0

# Main game function
def game():
    global player_score, computer_score
    # Player specifies how many rounds they want to play for.
    # Player is prompted to continue playing when <--
    # all the rounds have been played.
    total_rounds = int(input("\n\nHow many rounds do you want to play? "))
    rounds = 0
    # Loops through game() until the rounds played is equal to the total rounds variable.
    while rounds != total_rounds:
        choices_list = ['rock', 'paper', 'scissors'] # Choices available to computer and player.
        abbrev_choices = ['r','p','s'] # Abbreviated list of choices.
        
        ai_turn = random.choice(choices_list) # computer randomly chooses from the list.
        player_turn = input("\nChoose your move [rock, paper, scissors]: ").lower() # Player chooses their move and is stored as lowercase for list matching.
        # Players turn is matched to the choices list and the index of that element <---
        # is matched to the corresponding index in the abbreviated choices list <--
        # the abbreviated version of the players choice is stored into the player turn variable <--
        # allows the player to only input the first letter of their choice.
        if player_turn in abbrev_choices:
            abbrev_fix = abbrev_choices.index(player_turn)
            player_turn = choices_list[abbrev_fix]
        # prints a string when invalid input is used then continues executing.
        if player_turn not in choices_list:
            print('That is not a valid move. Try again.')
            continue
        # Calls the who_wins() function and stores data into the winner variable
        # The winners score is increased and the round is accounted for
        # Once the rounds played matches the total rounds the end_game() function is called <--
        # Player with the highest score wins
        winner = who_wins(player_turn, ai_turn)
        if winner == 'player':
            player_score += 1
            rounds += 1
            print('\n\nPlayer wins round: ', computer_score, 'vs', player_score)
        elif winner == 'computer':  
            computer_score += 1
            rounds += 1
            print('\n\nComputer wins round: ', computer_score, 'vs', player_score)
        if rounds == total_rounds:
            print('Player won:', player_score, 'rounds.'
                '\ncomputer won:', computer_score, 'rounds.')                  
            if player_score > computer_score:
                print('\n=== Player has won the game! === ')
                end_game()
                
                    
            else:
                print('\n=== Computer has won the game! ===')
                end_game()

# Function logic to determine the winner of each round
# Includes wins, losses and draws.
def who_wins(player_turn, ai_turn):
    if player_turn == 'rock' and ai_turn == 'scissors':
        print(
            '\nPlayer chose:', player_turn.upper(),
            '\nComputer chose:', ai_turn.upper(),
        )
        return 'player'
    elif player_turn == 'paper' and ai_turn == 'rock':
        print(
            '\nPlayer chose:', player_turn.upper(),
            '\nComputer chose:', ai_turn.upper(),
        )
        return 'player'
    elif player_turn == 'scissors' and ai_turn == 'paper':
        print(
            '\nPlayer chose:', player_turn.upper(),
            '\nComputer chose:', ai_turn.upper(),
        )
        return 'player'
    elif player_turn == 'rock' and ai_turn == 'paper':
        print(
            '\nPlayer chose:', player_turn.upper(),
            '\nComputer chose:', ai_turn.upper(),
        )
        return 'computer'
    elif player_turn == 'paper' and ai_turn == 'scissors':
        print(
            '\nPlayer chose:', player_turn.upper(),
            '\nComputer chose:', ai_turn.upper(),
        )
        return 'computer'
    elif player_turn == 'scissors' and ai_turn == 'rock':
        print(
            '\nPlayer chose:', player_turn.upper(),
            '\nComputer chose:', ai_turn.upper(),
        )
        return 'computer'
    elif player_turn == 'rock' and ai_turn == 'rock':
        print(
            'Player chose:', player_turn.upper(),
            '\nComputer chose:', ai_turn.upper(),
            '\n\nIts a draw!', player_score, 'vs', computer_score
        )
        return 'draw'
    elif player_turn == 'scissors' and ai_turn == 'scissors':
        print(
            'Player chose:', player_turn.upper(),
            '\nComputer chose:', ai_turn.upper(),
            '\n\nIts a draw!', player_score, 'vs', computer_score
        )
        return 'draw'
    elif player_turn == 'paper' and ai_turn == 'paper':
        print(
            'Player chose:', player_turn.upper(),
            '\nComputer chose:', ai_turn.upper(),
            '\n\nIts a draw!', player_score, 'vs', computer_score
        )
        return 'draw'

# End of game function that prompts the player to continue playing or not.
# Resets the player and computer scores for the next game.
def end_game():
    while True:
        global player_score, computer_score
        player_score = 0
        computer_score = 0
        play_again = str(input("\nWould you like to keep playing? ")).lower()
        if play_again.startswith('y'):
                game()
        if play_again.startswith('n'):
                print("Player has left the game.")
        break
game()