# Hot and Cold game
# Ahnaf Jabir Mir
# Last Modified on 2023-04-07
import random

MAX_LIVES = 5
MAX_RANGE = 25
MIN_RANGE = 5

cpu_num = 0
guess = 0
score = 0
lives = MAX_LIVES

def set_cpu_number():
    '''This function sets the number the player has to guess from a random int within the range specified by the CONSTANTS MIN_RANGE and MAX_RANGE'''
    global cpu_num
    cpu_num = random.randint(MIN_RANGE, MAX_RANGE)

def restoreLives():
    '''This function sets the number of lives back to the value defined by MAX_LIVES'''
    global lives
    lives = MAX_LIVES

def lowerLives():
    '''This function lowers the numbers of lives by one, and prints out how many lives are remaining'''
    global lives
    lives -= 1
    print(f"Lives Remaining: {lives}")

def update_score():
    '''This function raises the score by 1'''
    global score
    score += 1

def write_score():
    '''This function will attempt to append the player's current score into a txt file score_sheet.txt If an error occurs it will print out a message instead.'''
    try:
        score_sheet = open("score_sheet.txt", "a")
        score_sheet.write(f"\nHot and Cold score achieved in this session: {score}")
        score_sheet.close()
    except:
        print("An error has occured with the file!")

def compare_guess(guess: int, num: int) -> bool:
    '''This function compares the player's guess to the number the cpu has chosen. If the guess is lower than the number it will print out cold, if higher it will print out hot.
        if the player is close, it will specify by adding 'Tad bit' before hot or cold. It will return true if the player guessed the number correctly, or false if they did not.
        
            Parameters: guess int: an Integer
                        num int:   an Integer
                        
            Returns: boolean
    '''
    difference = num - guess
    if difference == 0:
        return True
    elif difference <= 3 and difference > 0:
        print("Tad bit cold! The number is slightly higher than your guess")
    elif difference >= -3 and difference < 0:
        print("Tad bit hot! The number is slightly lower than your guess")
    elif difference > 0:
        print("Cold! The number is higher than what you guessed")
    else:
        print("Hot! The number is lower than what you guessed")
    
    lowerLives()
    return False

def validate_guess(user_input:str) -> bool:
    '''This function checks if the player entered a number, if they did it will return true, if not it will return false
    
            Parameters: user_input str: a String
            
            Returns: boolean
    '''
    global guess
    if user_input.isnumeric():
        guess = int(user_input)
        if guess >= MIN_RANGE and guess <= MAX_RANGE:
            return True
        else:
            print("Guess not within specified range!")
            return False
    else:
        print("Guess is not a whole number!")
        return False

def get_guess() -> str:
    '''This function gets the user's guess as an input after prompting them with a message and then returns it.
    
            Return: user_guess str: a String
    '''
    user_guess = input("Guess: ")
    return user_guess
    
def game_intro():
    '''This function prints a welcome message, and sets the cpu to hold a number to guess'''

    print("Welcome to Hot and Cold! Try to guess the number the CPU picked between 5 and 25! You have 5 Guesses!")
    set_cpu_number()

def play_again() -> bool:
    '''This function will ask the user if they want to keep playing and return true or false depending on the input y, or n. It will loop until a correct input is received.
        If the user wants to keep playing, it will restore the lives, and set a new number to guess. If the user quits, it will write the score to the score_sheet.txt file.
    
            Returns: bool: a Boolean
    '''
    while True:
        user_desire = input("Keep Playing? Yes (Y) or No (N) ").capitalize()
        if user_desire == "Y" or user_desire == "Yes":
            restoreLives()
            set_cpu_number()
            return False
        elif user_desire == "N" or user_desire == "No":
            write_score()
            return True
        else:
            print("Invalid Input, Please enter Yes (Y) to quit, or No (N) to keep playing")

def game_over(lives:int):
    '''This function takes the number of lives as input and informs the user if they got the number or if they ran out of lives before guessing it. It will then always display
       what the number the cpu holding was and the player's current score.
       
            Parameters: lives int: an Integer
    '''
    if lives > 0: 
        update_score()
        print("You got it!")
    else:
        print(f"Outta lives!")
    
    print(f"The number was {cpu_num}")
    print(f"Current Score: {score}")
    
def run_game():
    '''This function runs the game by calling previously defined function in succession, it will loop forever until the user wishes to exit after a game.'''
    
    global cpu_num
    global guess
    global lives
    want_to_quit = False

    game_intro()
    while want_to_quit == False:
        guess = get_guess()
        if validate_guess(guess):
            guess_correct = compare_guess(guess, cpu_num)
            if guess_correct == True or lives == 0:
                game_over(lives)
                want_to_quit = play_again()
                