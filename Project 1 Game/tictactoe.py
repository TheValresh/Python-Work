# Tic tac toe game
# Ahnaf Jabir Mir
# Last Modified on 2023-04-07
import random

#SPACE_CLEAR = {0}
#BOARD_CLEAR = {1: ' ', 2: ' ', 3: ' ',
#         4: ' ', 5: ' ', 6: ' ',
#         7: ' ', 8: ' ', 9: ' '}

WINNING_COMBINATIONS = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

player_spaces = {0}
cpu_spaces = {0}
score = 0
total_spaces_taken = 0
want_to_quit = False

def render():
    '''This function prints the current board state on screen.'''
    global board
    i = 1

    while i < 10:
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("- + - + -")
        i += 3

def reset_board():
    '''This function wipes the board and player/cpu spaces 'clean' so a new game can be played.'''
    global board
    global player_spaces
    global cpu_spaces
    global total_spaces_taken

    board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
    player_spaces =  {0}
    cpu_spaces =  {0}
    total_spaces_taken = 0

def update_score():
    '''This function increments the score by 1'''
    global score

    score += 1

def write_score():
    '''This function will attempt to write the score into a txt file called score_sheet.txt'''
    try:
        score_sheet = open("score_sheet.txt", "a")
        score_sheet.write(f"\nTic Tac Toe Score achieved in this session: {score}")
        score_sheet.close()
    except:
        print("An error has occured with the file!")

def get_cpu_action() -> str:
    '''This function will randomly generate a number from 1-9 and return as a string. This is used for the cpu phase when it is determining a move.
    
            Returns str: String'''
    return str(random.randint(1, 9))

def get_action() -> str:
    '''This function prompts the user to speciify which space they wish to claim and returns it as a string
    
            Returns str: String'''
    return input("Please enter the space you wish to take: ")

def space_open(position: int) -> bool:
    '''This function will check if a space on the board at the given position is open or not. If not will return False, and return True otherwise. 
        A free space is denoted by the string ' '
                
                Parameters: position int: an Integer
                
                Returns: bool: a Boolean
    '''
    global board

    if board[position] == ' ':
        return True
    
    return False
    
def validate_action(action:str, player:str) -> bool:
    '''This function validates if the move given in the parameter is possible. It will first check if the input is numerical. 
        Then it will check if the input is within and range and the position is open. If yes, it will return true, else it will return false.
        If cpu is passed as the second string, it will not display the messages to avoid flooding the screen with random inputs.
        
                Parameters: action str: a String
                            player str: a String
                            
                Return:     bool: a Boolean
    '''
    if action.isnumeric():
        position = int(action)
        if position <= 9 and position >= 1 and space_open(position):
           return True
        else:
            if player == "player":
                print('You must pick one of the unoccupied spaces! (Between 1 and 9)')
    else:
        if player == "player":
            print('Input is not a numeric value')
    
    return False

def take_space(action:str, player:str):
    '''This function will take a position on the board and update the set of claimed spaces for the player. The board will also reflect this by replacing the empty
        space with a X if the player claims the spot, or a O if the CPU takes it.
        
                Parameters: action str: a String
                            player str: a String
    '''
    global player_spaces
    global cpu_spaces
    global board
    position = int(action)

    if player == "player":
        player_spaces.add(position)
        board[position] = 'X'
    elif player == "cpu":
        cpu_spaces.add(position)
        board[position] = 'O'

def check_win(player: str) -> bool:
    '''This function will check if the player or cpu wins by comparing the spaces they occupied to potential winning combination. If one of the combinations is a subset
        of the player's occupied spaces, they won and the function will return true. If none of the winning combinations are found as a subset of the players occupied
        spaces it will return false instead.
        
                Parameters: player str: a String
                
                Returns: bool: a Boolean
    '''
    global player_spaces
    global cpu_spaces
    global WINNING_COMBINATIONS

    if player == "player":
        for win_combo in WINNING_COMBINATIONS:
            if win_combo.issubset(player_spaces):
                return True
    elif player == "cpu":
        for win_combo in WINNING_COMBINATIONS:
            if win_combo.issubset(cpu_spaces):
                return True
            
    return False
    
def play_again() -> bool:
    '''This function will ask if the player wishes to continue playing, if y, Y, or Yes is entered it will return false, if No, n, or N is entered it will
        write the current score and return false. This will loop until a proper input is received.
        
                Returns: bool: a Boolean
    '''
    while True:
        user_desire = input("Keep Playing? Yes (Y) or No (N) ").capitalize()
        if user_desire == "Y" or user_desire == "Yes":
            return False
        elif user_desire == "N" or user_desire == "No":
            write_score()
            return True
        else:
            print("Invalid Input, Please enter Yes (Y) to quit, or No (N) to keep playing")

def game_over(winner:str):
    '''This function will take the given parameter as the winner, if it is the player it will congratulate them and display there score after updating it. If the cpu
        won, it will reprimand the player, and if it was a tie will delcare so. Afterwards the board is reset, and the player is asked if they want to continue.
        
                Parameters: winner str: a String
    '''
    global want_to_quit

    if winner == "player":
        update_score()
        print(f"You won! Current score is: {score}")
    elif winner == "cpu":
        print("You lost!")
    else:
        print("Tie!")
        
    reset_board()
    want_to_quit = play_again()

def resolve_winner(winner:str):
    '''This function will check if the conditions for a winner has been acheived, and will render the game winning board layout and call game over with the winner passed
        as the argument.
                
                Parameters: winner str: a String
    '''

    if check_win(winner):
        render()
        game_over(winner)

def resolve_tie():
    '''This function checks if a tie has occured, in which all 9 spaces are taken but no winning combinations were acheived. If yes, it will call game_over passed with
        tie as an argument.'''
    global total_spaces_taken

    if total_spaces_taken == 9:
        game_over("tie")

def player_phase():
    '''This function facilitates the player phase of the game. It will first get an action from the player and validate it. If the action is no valid it will loop until it
        gets an acceptable action. Afterwards it will take the space and claim it has the players. Afterwards total_spaces_taken will be incremented by 1. After all of this
        it will check and try to resolve if the player has a winning combinations.'''
    global total_spaces_taken

    action = get_action()
    while validate_action(action, "player") == False:
        action = get_action()
    
    take_space(action, "player")
    total_spaces_taken += 1

    resolve_winner("player")

def cpu_phase():
    '''This function facilitates the cpu phase of the game. It will first get an action from the cpu and validate it. If the action is no valid it will loop until it
        gets an acceptable action. Afterwards it will take the space and claim it has the cpu's. Afterwards total_spaces_taken will be incremented by 1. After all of this
        it will check and try to resolve if the cpu has a winning combinations.'''
    global total_spaces_taken

    cpu_action = get_cpu_action()
    while validate_action(cpu_action, "cpu") == False:
        cpu_action = get_cpu_action()

    take_space(cpu_action, "cpu")
    total_spaces_taken += 1

    resolve_winner("cpu")

def game_intro():
    '''This function prints a welcome message and informs the user how to play the game'''
    print("Welcome to Tic Tac Toe!")
    print("The spaces on the board are noted as:")
    i = 1

    while i < 10:
        print(f"{i} | {i+1} | {i+2}")
        if i < 6:
            print("- + - + -")
        i += 3
    print("Good Luck!\n")

def run_game():
    '''This function runs the game by calling functions in sucession. It will greet the user with the intro, then render the board. It then conducts the player phase
        followed by the cpu phase. It will check if a tie has occured after each 'full turn'. It will loop until the user wishes to exit after a match.'''
    game_intro()
    while want_to_quit == False:
        render()

        player_phase()
        cpu_phase()

        resolve_tie()