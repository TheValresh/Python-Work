import sys
import hot_and_cold
import rps_game
import tictactoe

def main():
    menu()

def menu():
    print('Welcome to Ahnaf Jabir Mir\'s 3 games')
    user_input = input("A. To play Rock, Paper, Scissors\nB. To play Hot and Cold\nC. To play Tic-Tac-Toe\nQ. To quit\n")

    if user_input == "A" or user_input == "a":
        start_rps()
    elif user_input == "B" or user_input == "b":
        start_hnc()
    elif user_input == "C" or user_input == "c":
        start_ttt()
    elif user_input == "Q" or user_input == "q":
        sys.exit()
    else:
        print("Please select A, B, or C")
    
    menu()

def start_hnc():
    hot_and_cold.run_game()

def start_rps():
    rps_game.run_game()

def start_ttt():
    tictactoe.run_game()

main()