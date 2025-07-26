import pyfiglet
import random
from colorama import Fore, Style
from prettytable import PrettyTable
import datetime
import os
from functools import reduce
import math
import webbrowser

# SHUTDOWN COMMAND
def shutdown():
    print(f"{Fore.MAGENTA}---miniOS 0.0.1 shut down---{Style.RESET_ALL}")

# NEW SCREEN FUNCTION
def new_screen():
    os.system("cls" if os.name == "nt" else "clear")


# USER FILES
user_files = {}

# USER NOTES
user_notes = {}

# COMMAND FUNCTION
def command_function():
    while True:
        command = input("User > ")
        if command == "exit":
            desktop_menu()
            return
        elif command == "help":
            print("""Minicustom available commands (miniOS version 0.0.1)
        help --- displays this screen
        clear --- clears all commands on the screen
        info --- displays info about miniOS
        files --- displays all your current files
        exit --- exits to the desktop menu
        shutdown --- shutdown miniOS
        """)
        elif command == "clear":
            new_screen()
            mini_custom_title = pyfiglet.figlet_format("Minicustom")
            print(mini_custom_title)
            command_function()
            return
        elif command == "info":
            print("""miniOS current version: 0.0.1
        Early Supporters:
            stierprogrammer --- discord
            gudetimo --- discord

        Creator of miniOS:
            penguinguy25 --- replit and discord

        Language: Python""")
        elif command == "files":
            print(f"Current files: {user_files}")
        elif command == "shutdown":
            shutdown()
            return
        else:
            print("Command invalid. Type help for a list of commands.")

# MINICUSTOM
def mini_custom():
    new_screen()
    mini_custom_title = pyfiglet.figlet_format("Minicustom")
    print(mini_custom_title)
    command_function()
        


# LINK FUNCTION
def link_function():
    print(f"{Fore.LIGHTGREEN_EX}Type your URL down below . . .")
    while True:
        url = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if url == "exit":
            desktop_menu()
            return
        else:
            open_link(url)
            print(f"{Fore.LIGHTGREEN_EX}Tab opened! Open another link? y/n")
            while True:
                another_link = input(f"{Fore.RED}> {Style.RESET_ALL}")
                if another_link == "y":
                    print(f"{Fore.LIGHTGREEN_EX}Type your URL down below . . .{Style.RESET_ALL}")
                    break
                elif another_link == "n":
                    video_player()
                    return
                else:
                    print(f"{Fore.RED}That option doesn't exist! Please type either y or n.{Style.RESET_ALL}")

# LINK OPENER
def open_link(url):
    webbrowser.open(url)

# VIDEO PLAYER
def video_player():
    new_screen()
    video_player_title = pyfiglet.figlet_format("Video Player")
    print(f"{Fore.LIGHTGREEN_EX}{video_player_title}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTRED_EX}This app is still in Beta! Features are not fully completed.{Style.RESET_ALL}")
    print("--------------------------------------------------------")
    print(f"{Fore.LIGHTGREEN_EX}To use Video Player, type a URL down below and a tab will open in your default browser with that link. Be careful when typing the link, don't enter unverified links! If the newly opened tab looks empty, try checking if you wrote the link correctly. Type exit to exit.")
    link_function()
    
    


# MATH FUNCTION
def math_function(num, difficulty):
    print(f"{Fore.GREEN}{difficulty}{Fore.LIGHTBLUE_EX} difficulty selected. Answer the questions below:")
    while True:
        first_number = random.randint(int(num / 2), num)
        second_number = random.randint(int(num / 2), num)
        print(f"{Fore.LIGHTYELLOW_EX}{first_number} + {second_number} = . . .")
        try:
            math_answer = input(f"{Fore.RED}> {Style.RESET_ALL}")
            if math_answer == "exit":
                math_training()
                return
            answer = int(math_answer)
            if answer == first_number + second_number:
                print(f"{Fore.GREEN}--------{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
                print(f"{Fore.GREEN}--------{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}-------------{Style.RESET_ALL}")
                print(f"{Fore.RED}Wrong answer!{Style.RESET_ALL}")
                print(f"{Fore.RED}-------------{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}That's not a number!{Style.RESET_ALL}")
        
    


# MATH TRAINING
def math_training():
    math_title = pyfiglet.figlet_format("Math Training")
    print(f"{Fore.LIGHTCYAN_EX}{math_title}{Style.RESET_ALL}")
    math_table = PrettyTable()
    math_table.field_names = [f"{Fore.LIGHTCYAN_EX}Index{Style.RESET_ALL}", f"{Fore.GREEN}Difficulty{Style.RESET_ALL}"]
    math_table.add_row([f"{Fore.LIGHTCYAN_EX}1{Style.RESET_ALL}", f"{Fore.LIGHTGREEN_EX}Easy{Style.RESET_ALL}"])
    math_table.add_row([f"{Fore.LIGHTCYAN_EX}2{Style.RESET_ALL}", f"{Fore.YELLOW}Normal{Style.RESET_ALL}"])
    math_table.add_row([f"{Fore.LIGHTCYAN_EX}3{Style.RESET_ALL}", f"{Fore.LIGHTRED_EX}Hard{Style.RESET_ALL}"])
    math_table.add_row([f"{Fore.LIGHTCYAN_EX}4{Style.RESET_ALL}", f"{Fore.RED}Extreme{Style.RESET_ALL}"])
    math_table.add_row([f"{Fore.LIGHTCYAN_EX}5{Style.RESET_ALL}", f"{Fore.LIGHTMAGENTA_EX}Legendary{Style.RESET_ALL}"])
    print(math_table)
    print(f"{Fore.LIGHTCYAN_EX}Select the difficulty you want by typing its index. You will then be given math questions to that difficulty level (addition only){Style.RESET_ALL}")
    while True:
        math_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if math_choice == "exit":
            minigames()
            return
        elif math_choice == "1":
            math_function(10, "Easy")
            return
        elif math_choice == "2":
            math_function(100, "Normal")
            return
        elif math_choice == "3":
            math_function(500, "Hard")
            return
        elif math_choice == "4":
            math_function(3000, "Extreme")
            return
        elif math_choice == "5":
            math_function(30245, "Legendary")
            return
        


# GUESS FUNCTION
def guess_function(number):
    selected_number = random.randint(1, number)
    print(f"{Fore.LIGHTGREEN_EX}A random number from 1-{number} has been selected. Try guessing it below:")
    while True:
        guess_number = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if guess_number == "exit":
            guess_the_number()
            return
        try:
            integer = int(guess_number)
            if integer > number:
                print(f"{Fore.RED}That number's too big! The scale is from 1-{number}!{Style.RESET_ALL}")
            elif integer < 1:
                print(f"{Fore.RED}That number's too small! The scale is from 1-{number}!{Style.RESET_ALL}")
            elif integer < selected_number:
                print(f"{Fore.LIGHTRED_EX}Higher...{Style.RESET_ALL}")
            elif integer > selected_number:
                print(f"{Fore.LIGHTBLUE_EX}Lower...")
            elif integer == selected_number:
                print(f"{Fore.GREEN}You guessed correctly! The number was indeed {selected_number}!{Style.RESET_ALL}")
                print(f"{Fore.LIGHTGREEN_EX}Play again? y/n{Style.RESET_ALL}")
                while True:
                    play_input = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_input == "y":
                        guess_function(number)
                        return
                    elif play_input == "n":
                        guess_the_number()
                        return
                    else:
                        print(f"{Fore.RED}That's not a valid option! Please type either y or n.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}That's not a valid number!{Style.RESET_ALL}")
penguinguy25 = "Username of the creator of miniOS on Discord and Replit"
# GUESS THE NUMBER
def guess_the_number():
    guess_the_number_title = pyfiglet.figlet_format("Guess ").splitlines()
    guess_the_number_title_2 = pyfiglet.figlet_format("the ").splitlines()
    guess_the_number_title_3 = pyfiglet.figlet_format("Number").splitlines()
    for cooltitle1, cooltitle2, cooltitle3 in zip(guess_the_number_title, guess_the_number_title_2, guess_the_number_title_3):
        print(f"{Fore.LIGHTGREEN_EX}{cooltitle1}{cooltitle2}{cooltitle3}{Style.RESET_ALL}")
    guess_table = PrettyTable()
    guess_table.field_names = [f"{Fore.LIGHTCYAN_EX}Index{Style.RESET_ALL}", f"{Fore.LIGHTGREEN_EX}Amount{Style.RESET_ALL}"]
    guess_table.add_row([f"{Fore.LIGHTCYAN_EX}1{Style.RESET_ALL}", f"{Fore.LIGHTGREEN_EX}10{Style.RESET_ALL}"])  
    guess_table.add_row([f"{Fore.LIGHTCYAN_EX}2{Style.RESET_ALL}", f"{Fore.LIGHTGREEN_EX}100{Style.RESET_ALL}"])
    guess_table.add_row([f"{Fore.LIGHTCYAN_EX}3{Style.RESET_ALL}", f"{Fore.LIGHTGREEN_EX}1000{Style.RESET_ALL}"])
    guess_table.add_row([f"{Fore.LIGHTCYAN_EX}4{Style.RESET_ALL}", f"{Fore.LIGHTGREEN_EX}10000{Style.RESET_ALL}"])
    print(guess_table)
    print(f"{Fore.LIGHTGREEN_EX}The amount of numbers determines the max number that the computer can randomly select.")
    print(f"{Fore.LIGHTGREEN_EX}Select the amount you want by typing the index . . .")
    while True:
        guess_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if guess_choice == "1":
            guess_function(10)
            return
        elif guess_choice == "2":
            guess_function(100)
            return
        elif guess_choice == "3":
            guess_function(1000)
            return
        elif guess_choice == "4":
            guess_function(10000)
            return
        elif guess_choice == "exit":
            desktop_menu()
            return
        else:
            print(f"{Fore.RED}That's not an available command!{Style.RESET_ALL}")


# ROCK PAPER SCISSORS FUNCTION
def rock_paper_scissors_function():
    print(f"Type either {Fore.CYAN}Rock{Style.RESET_ALL}, Paper or {Fore.RED}Scissors{Style.RESET_ALL} to continue . . .")
    print(f"{Fore.LIGHTBLACK_EX}(case insensitive){Style.RESET_ALL}")
    while True:
        game1_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        game1_choice = game1_choice.lower()
        if game1_choice == "rock":
            computer_choice = random.choice(computer_choices)
            if computer_choice == "paper":
                print(f"{Fore.RED}The computer chose paper. Paper beats rock, you lost!{Style.RESET_ALL}")
                print("Play again? y/n")
                while True:
                    play_again = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_again == "y":
                        rock_paper_scissors_function()
                        return
                    elif play_again == "n":
                        minigames()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.")
            elif computer_choice == "rock":
                print("The computer also chose rock, you drew!")
                print("Play again? y/n")
                while True:
                    play_again2 = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_again2 == "y":
                        rock_paper_scissors_function()
                        return
                    elif play_again2 == "n":
                        minigames()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.")
            else:
                print(f"{Fore.GREEN}The computer chose scissors. Rock beats scissors, you won!{Style.RESET_ALL}")
                print("Play again? y/n")
                while True:
                    play_again3 = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_again3 == "y":
                        rock_paper_scissors_function()
                        return
                    elif play_again3 == "n":
                        minigames()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.")
        elif game1_choice == "paper":
            computer_choice = random.choice(computer_choices)
            if computer_choice == "paper":
                print(f"{Fore.RED}The computer also chose paper, you drew!{Style.RESET_ALL}")
                print("Play again? y/n")
                while True:
                    play_again = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_again == "y":
                        rock_paper_scissors_function()
                        return
                    elif play_again == "n":
                        minigames()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.")
            elif computer_choice == "rock":
                print(f"{Fore.GREEN}The computer chose rock. Paper beats rock, you won!{Style.RESET_ALL}")
                print("Play again? y/n")
                while True:
                    play_again2 = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_again2 == "y":
                        rock_paper_scissors_function()
                        return
                    elif play_again2 == "n":
                        minigames()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.")
            else:
                print(f"{Fore.RED}The computer chose scissors. Scissors beats paper, you lost!{Style.RESET_ALL}")
                print("Play again? y/n")
                while True:
                    play_again3 = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_again3 == "y":
                        rock_paper_scissors_function()
                        return
                    elif play_again3 == "n":
                        minigames()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.")
        elif game1_choice == "scissors":
            computer_choice = random.choice(computer_choices)
            if computer_choice == "paper":
                print(f"{Fore.GREEN}The computer chose paper. Scissors beats paper, you won!{Style.RESET_ALL}")
                print("Play again? y/n")
                while True:
                    play_again = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_again == "y":
                        rock_paper_scissors_function()
                        return
                    elif play_again == "n":
                        minigames()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.")
            elif computer_choice == "rock":
                print(f"{Fore.RED}The computer chose rock. Rock beats scissors, you lost!{Style.RESET_ALL}")
                print("Play again? y/n")
                while True:
                    play_again2 = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_again2 == "y":
                        rock_paper_scissors_function()
                        return
                    elif play_again2 == "n":
                        minigames()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.{Style.RESET_ALL}")
            else:
                print("The computer also chose scissors, you drew!")
                print("Play again? y/n")
                while True:
                    play_again3 = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if play_again3 == "y":
                        rock_paper_scissors_function()
                        return
                    elif play_again3 == "n":
                        minigames()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.")
        elif game1_choice == "exit":
            minigames()
            return
        else:
            print(f"{Fore.RED}That's not an option!{Style.RESET_ALL}")


computer_choices = ["rock", "paper", "scissors"]


# ROCK PAPER SCISSORS
def rock_paper_scissors():
    rock_paper_scissors_title_1 = pyfiglet.figlet_format("Rock").splitlines()
    comma_title = pyfiglet.figlet_format(", ").splitlines()
    rock_paper_scissors_title_2 = pyfiglet.figlet_format("Paper").splitlines()
    rock_paper_scissors_title_3 = pyfiglet.figlet_format(
        "Scissors").splitlines()
    for rock, comma, paper, scissors in zip(rock_paper_scissors_title_1, comma_title, rock_paper_scissors_title_2, rock_paper_scissors_title_3):
        print(f"{Fore.CYAN}{rock}{Fore.LIGHTBLACK_EX}{comma}{Style.RESET_ALL}{paper}{Fore.LIGHTBLACK_EX}{comma}{Fore.RED}{scissors}{Style.RESET_ALL}")
    rock_paper_scissors_function()


# MINIGAMES
def minigames():
    new_screen()
    minigames_title = pyfiglet.figlet_format("Minigames")
    print(f"{Fore.MAGENTA}{minigames_title}{Style.RESET_ALL}")
    minigame_list = PrettyTable()
    minigame_list.field_names = [f"{Fore.LIGHTCYAN_EX}Index{Style.RESET_ALL}", f"{Fore.MAGENTA}Game{Style.RESET_ALL}"]
    minigame_list.add_row([f"{Fore.LIGHTCYAN_EX}1{Style.RESET_ALL}", f"{Fore.MAGENTA}Rock, Paper, Scissors{Style.RESET_ALL}"])
    minigame_list.add_row([f"{Fore.LIGHTCYAN_EX}2{Style.RESET_ALL}", f"{Fore.MAGENTA}Guess the Number{Style.RESET_ALL}"])
    minigame_list.add_row([f"{Fore.LIGHTCYAN_EX}3{Style.RESET_ALL}", f"{Fore.MAGENTA}Math Training{Style.RESET_ALL}"])
    print(minigame_list)
    print(f"{Fore.MAGENTA}Type the index of a minigame to play . . .{Style.RESET_ALL}")
    while True:
        minigame_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if minigame_choice == "1":
            rock_paper_scissors()
            return
        elif minigame_choice == "2":
            guess_the_number()
            return
        elif minigame_choice == "3":
            math_training()
            return
        elif minigame_choice == "exit":
            desktop_menu()
            return
        else:
            print(f"{Fore.RED}That's not a command!{Style.RESET_ALL}")


# CLEAR FUNCTIONS
def clear_function_addition():
    user_operation.clear()
    addition_function()


def clear_function_substraction():
    user_operation.clear()
    substraction_function()


def clear_function_multiplication():
    user_operation.clear()
    multiplication_function()


def clear_function_division():
    user_operation.clear()
    division_function()


# DIVISION FUNCTION
def division_function():
    if len(user_operation) >= 2:
        division_current_result = reduce(lambda x, y: x / y, user_operation)
        print(f"{Fore.LIGHTBLACK_EX}Current result: {division_current_result}{Style.RESET_ALL}")
    elif len(user_operation) == 1:
        division_current_result = user_operation[0]
        print(f"{Fore.LIGHTBLACK_EX}Current result: {division_current_result}{Style.RESET_ALL}")
    else:
        division_current_result = 0
        print(f"{Fore.LIGHTBLACK_EX}Current result: {division_current_result}{Style.RESET_ALL}")
    try:
        print(f"{Fore.CYAN}Enter a number, type '=' to  type exit to exit . . .{Style.RESET_ALL}")
        while True:
            division_number = input(f"{Fore.RED}> {Style.RESET_ALL}")
            if division_number == "exit":
                calculator()
                return
            elif division_number == "=":
                if len(user_operation) >= 2:
                    result = reduce(lambda x, y: x / y, user_operation)
                    print(f"{Fore.CYAN}The result of {user_operation} is {Fore.LIGHTGREEN_EX}{result}{Style.RESET_ALL}")
                elif len(user_operation) == 1:
                    result = user_operation[0]
                    print(f"{Fore.CYAN}The result of {user_operation} is {Fore.LIGHTGREEN_EX}{result}{Style.RESET_ALL}")
                else:
                    result = 0
                    print(f"{Fore.CYAN}The result of {user_operation} is {Fore.LIGHTGREEN_EX}{result}{Style.RESET_ALL}")

                print(f"{Fore.CYAN}Perform another division? y/n")
                while True:
                    another_division = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if another_division == "y":
                        clear_function_division()
                        return
                    elif another_division == "n":
                        calculator()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.{Style.RESET_ALL}")
            else:
                try:
                    user_operation.append(float(division_number))
                    if len(user_operation) >= 2:
                        division_current_result = reduce(
                            lambda x, y: x / y, user_operation)
                    elif len(user_operation) == 1:
                        division_current_result = user_operation[0]
                    else:
                        division_current_result = 0
                    print(f"{Fore.LIGHTBLACK_EX}Current result: {division_current_result}{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}. . .{Style.RESET_ALL}")
                except ZeroDivisionError:
                    print(f"{Fore.RED}You can't divide by zero!{Style.RESET_ALL}")
                    user_operation.pop()

    except ValueError:
        print(f"{Fore.RED}That's not a number!{Style.RESET_ALL}")
        division_function()
        return


# MULTIPLICATION FUNCTION
def multiplication_function():
    if not user_operation:
        multiplication_current_result = 0
    else:
        multiplication_current_result = math.prod(user_operation)
    print(f"{Fore.LIGHTBLACK_EX}Current result: {multiplication_current_result}")
    try:
        print(f"{Fore.CYAN}Enter a number, type '=' to  type exit to exit . . .{Style.RESET_ALL}")
        while True:
            multiplication_number = input(f"{Fore.RED}> {Style.RESET_ALL}")
            if multiplication_number == "exit":
                calculator()
                return
            elif multiplication_number == "=":
                print(f"{Fore.CYAN}The result of {user_operation} is {Fore.LIGHTGREEN_EX}{math.prod(user_operation)}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Perform another multiplication? y/n")
                while True:
                    another_multiplication = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if another_multiplication == "y":
                        clear_function_multiplication()
                        return
                    elif another_multiplication == "n":
                        calculator()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.{Style.RESET_ALL}")
            else:
                user_operation.append(float(multiplication_number))
                multiplication_current_result = math.prod(user_operation)
                print(f"{Fore.LIGHTBLACK_EX}Current result: {multiplication_current_result}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}. . .{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}That's not a number!{Style.RESET_ALL}")
        multiplication_function()
        return


# SUBSTRACTION FUNCTION
def substraction_function():
    if len(user_operation) >= 2:
        substraction_current_result = reduce(lambda x, y: x - y, user_operation)
        print(f"{Fore.LIGHTBLACK_EX}Current result: {substraction_current_result}{Style.RESET_ALL}")
    elif len(user_operation) == 1:
        substraction_current_result = user_operation[0]
        print(f"{Fore.LIGHTBLACK_EX}Current result: {substraction_current_result}{Style.RESET_ALL}")
    else:
        substraction_current_result = 0
        print(f"{Fore.LIGHTBLACK_EX}Current result: {substraction_current_result}{Style.RESET_ALL}")
    try:
        print(f"{Fore.CYAN}Enter a number, type '=' to  type exit to exit . . .{Style.RESET_ALL}")
        while True:
            substraction_number = input(f"{Fore.RED}> {Style.RESET_ALL}")
            if substraction_number == "exit":
                calculator()
                return
            elif substraction_number == "=":
                if len(user_operation) >= 2:
                    result = reduce(lambda x, y: x - y, user_operation)
                    print(f"{Fore.CYAN}The result of {user_operation} is {Fore.LIGHTGREEN_EX}{result}{Style.RESET_ALL}")
                elif len(user_operation) == 1:
                    result = user_operation[0]
                    print(f"{Fore.CYAN}The result of {user_operation} is {Fore.LIGHTGREEN_EX}{result}{Style.RESET_ALL}")
                else:
                    result = 0
                    print(f"{Fore.CYAN}The result of {user_operation} is {Fore.LIGHTGREEN_EX}{result}{Style.RESET_ALL}")

                print(f"{Fore.CYAN}Perform another substraction? y/n")
                while True:
                    another_substraction = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if another_substraction == "y":
                        clear_function_substraction()
                        return
                    elif another_substraction == "n":
                        calculator()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.{Style.RESET_ALL}")
            else:
                user_operation.append(float(substraction_number))
                if len(user_operation) >= 2:
                    substraction_current_result = reduce(lambda x, y: x - y, user_operation)
                elif len(user_operation) == 1:
                    substraction_current_result = user_operation[0]
                else:
                    substraction_current_result = 0
                print(f"{Fore.LIGHTBLACK_EX}Current result: {substraction_current_result}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}. . .{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}That's not a number!{Style.RESET_ALL}")
        substraction_function()
        return


# ADDITION FUNCTION
def addition_function():
    addition_current_result = sum(user_operation)
    print(f"{Fore.LIGHTBLACK_EX}Current result: {addition_current_result}")
    try:
        print(f"{Fore.CYAN}Enter a number, type '=' to  type exit to exit . . .{Style.RESET_ALL}")
        while True:
            addition_number = input(f"{Fore.RED}> {Style.RESET_ALL}")
            if addition_number == "exit":
                calculator()
                return
            elif addition_number == "=":
                print(f"{Fore.CYAN}The result of {user_operation} is {Fore.LIGHTGREEN_EX}{sum(user_operation)}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Perform another addition? y/n")
                while True:
                    another_addition = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if another_addition == "y":
                        clear_function_addition()
                        return
                    elif another_addition == "n":
                        calculator()
                        return
                    else:
                        print(f"{Fore.RED}That's not an option! Please choose either y or n.{Style.RESET_ALL}")
            else:
                user_operation.append(float(addition_number))
                addition_current_result = sum(user_operation)
                print(f"{Fore.LIGHTBLACK_EX}Current result: {addition_current_result}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}. . .{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}That's not a number!{Style.RESET_ALL}")
        addition_function()
        return


# USER OPERATIONS
user_operation = []


# CALCULATOR
def calculator():
    user_operation.clear()
    new_screen()
    calculator_title_1 = pyfiglet.figlet_format("Calcu").splitlines()
    calculator_title_2 = pyfiglet.figlet_format("lator").splitlines()

    for line1, line2 in zip(calculator_title_1, calculator_title_2):
        print(f"{Fore.CYAN}{line1}{Fore.RED}{line2}{Style.RESET_ALL}")
    operation_list = PrettyTable()
    operation_list.field_names = [f"{Fore.CYAN}Index{Style.RESET_ALL}", f"{Fore.CYAN}Operation{Style.RESET_ALL}", f"{Fore.RED}Action{Style.RESET_ALL}"]
    operation_list.add_row([f"{Fore.CYAN}1{Style.RESET_ALL}", f"{Fore.CYAN}+{Style.RESET_ALL}", f"{Fore.RED}Addition{Style.RESET_ALL}"])
    operation_list.add_row([f"{Fore.CYAN}2{Style.RESET_ALL}", f"{Fore.CYAN}-{Style.RESET_ALL}", f"{Fore.RED}Substraction{Style.RESET_ALL}"])
    operation_list.add_row([f"{Fore.CYAN}3{Style.RESET_ALL}", f"{Fore.CYAN}*{Style.RESET_ALL}", f"{Fore.RED}Multiplication{Style.RESET_ALL}"])
    operation_list.add_row([f"{Fore.CYAN}4{Style.RESET_ALL}", f"{Fore.CYAN}÷{Style.RESET_ALL}", f"{Fore.RED}Division{Style.RESET_ALL}"])
    print(operation_list)
    print(f"{Fore.CYAN}Type the index of an operation to continue . . .{Style.RESET_ALL}")
    while True:
        operation_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if operation_choice == "1":
            # ADDITION
            addition_function()
            return
        elif operation_choice == "2":
            # SUBSTRACTION
            substraction_function()
            return
        elif operation_choice == "3":
            # MULTIPLICATION
            multiplication_function()
            return
        elif operation_choice == "4":
            # DIVISION
            division_function()
            return
        elif operation_choice == "exit":
            desktop_menu()
            return
        else:
            print(f"{Fore.RED}That's not an option!{Style.RESET_ALL}")


def complete_another_task_function():

    to_do_notes_list_random = PrettyTable()
    to_do_notes_list_random.field_names = [f"{Fore.LIGHTMAGENTA_EX}Note name{Style.RESET_ALL}", f"{Fore.LIGHTMAGENTA_EX}Note contents{Style.RESET_ALL}", f"{Fore.LIGHTMAGENTA_EX}Time of creation{Style.RESET_ALL}"]

    for user_note, user_note_data in user_notes.items():
        to_do_notes_list_random.add_row([f"{Fore.LIGHTMAGENTA_EX}{user_note}{Style.RESET_ALL}", f"{Fore.LIGHTMAGENTA_EX}{user_note_data['short_content']}{Style.RESET_ALL}", f"{Fore.LIGHTMAGENTA_EX}{user_note_data['creation_time']}{Style.RESET_ALL}"])
    print(to_do_notes_list_random)
    print(f"{Fore.LIGHTMAGENTA_EX}Type the name of a note to complete it: {Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}(type exit\\ to exit){Style.RESET_ALL}")
    while True:
        complete_note = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if complete_note in user_notes:
            del user_notes[complete_note]
            print(f"{Fore.GREEN}Task completed.{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}Complete another task? y/n{Style.RESET_ALL}")
            while True:
                complete_another_task = input(f"{Fore.RED}> {Style.RESET_ALL}")
                if complete_another_task == "y":
                    complete_another_task_function()
                    break
                elif complete_another_task == "n":
                    to_do_list()
                    break
                else:
                    print(f"{Fore.RED}That's not an option! Please type either y or n.{Style.RESET_ALL}")
        elif complete_note == "exit\\":
            to_do_list()
            break
        else:
            print(f"{Fore.RED}That's not a command!{Style.RESET_ALL}")


def to_do_list_reminder_function():
    print(f"{Fore.LIGHTMAGENTA_EX}Write a reminder:{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}(type exit\\ to exit){Style.RESET_ALL}")
    while True:
        user_note = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if user_note == "exit\\":
            to_do_list()
        else:
            print(f"{Fore.LIGHTMAGENTA_EX}Enter a name for your reminder:{Style.RESET_ALL}")
            while True:
                reminder_name = input(f"{Fore.RED}> {Style.RESET_ALL}")
                short_user_note = (user_note[:20] + " . . .") if len(user_note) < 20 else user_note
                current_time = datetime.datetime.now()
                note_creation_time_1 = current_time.strftime("%H:%M")
                note_creation_time_2 = current_time.strftime("%d:%m:%Y")
                full_note_creation_time = note_creation_time_1 + " " + note_creation_time_2
                user_notes[reminder_name] = {
                    'full_content': user_note,
                    'short_content': short_user_note,
                    'creation_time': full_note_creation_time
                }
                print(f"{Fore.LIGHTMAGENTA_EX}File {Fore.GREEN}saved {Fore.LIGHTMAGENTA_EX}successfully!{Style.RESET_ALL}")
                print(f"{Fore.LIGHTMAGENTA_EX}Write another reminder? y/n{Style.RESET_ALL}")
                while True:
                    another_note_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
                    if another_note_choice == "y":
                        to_do_list_reminder_function()
                        break
                    elif another_note_choice == "n":
                        to_do_list()
                        break
                    else:
                        print(f"{Fore.RED}That's not an option! Please type either y or n.{Style.RESET_ALL}")


def to_do_list():
    new_screen()

    to_do_title = pyfiglet.figlet_format("To-do List")
    print(f"{Fore.LIGHTMAGENTA_EX}{to_do_title}{Style.RESET_ALL}")
    to_do_notes_list = PrettyTable()
    to_do_notes_list.field_names = [f"{Fore.LIGHTMAGENTA_EX}Note name{Style.RESET_ALL}", f"{Fore.LIGHTMAGENTA_EX}Note contents{Style.RESET_ALL}", f"{Fore.LIGHTMAGENTA_EX}Time of creation{Style.RESET_ALL}"]
    for user_note, user_note_data in user_notes.items():
        to_do_notes_list.add_row([f"{Fore.LIGHTMAGENTA_EX}{user_note}{Style.RESET_ALL}", f"{Fore.LIGHTMAGENTA_EX}{user_note_data['short_content']}{Style.RESET_ALL}", f"{Fore.LIGHTMAGENTA_EX}{user_note_data['creation_time']}{Style.RESET_ALL}"])
    print(to_do_notes_list)
    print(f"""{Fore.LIGHTMAGENTA_EX}Current commands:
    new --- create a new task
    done --- complete a task and remove it from the list
    {Style.RESET_ALL}""")
    print(f"{Fore.LIGHTBLACK_EX}(type the name of a task to access it. Type exit\\ to exit){Style.RESET_ALL}")
    while True:
        to_do_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if to_do_choice == "new":
            to_do_list_reminder_function()
        elif to_do_choice == "done":
            complete_another_task_function()
        elif to_do_choice == "exit\\":
            desktop_menu()
        elif to_do_choice in user_notes:
            note_data = user_notes[to_do_choice]
            print(f"{Fore.LIGHTMAGENTA_EX}Note name: {Fore.CYAN}{to_do_choice}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}\nNote contents: {Fore.GREEN}{note_data['full_content']}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTMAGENTA_EX}\nTime of creation: {Fore.CYAN}{note_data['creation_time']}{Style.RESET_ALL}")
            while True:
                exit_input = input(f"{Fore.RED}> {Style.RESET_ALL}")
                if exit_input == "exit":
                    to_do_list()
                else:
                    print(f"{Fore.RED}That's not a command! Type exit to exit.{Style.RESET_ALL}")


def text_editor_input():
    text_editor_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
    if text_editor_choice == "exit\\":
        desktop_menu()
        return
    print(f"{Fore.CYAN}Enter a name for your file:")
    while True:
        text_editor_file_name_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")

        if text_editor_file_name_choice + ".mwrt" in user_files:
            print(f"{Fore.RED}That file name already exists, please choose another name!{Style.RESET_ALL}")
            continue
        else:
            print(f"{Fore.GREEN}File saved!{Style.RESET_ALL}")
            time = datetime.datetime.now()
            file_creation_time_hourminute = time.strftime("%H:%M")
            file_creation_time_daymonthyear = time.strftime("%d:%m:%Y")
            file_creation_time = f"{file_creation_time_hourminute} {file_creation_time_daymonthyear}"
            text_editor_file_name_choice = text_editor_file_name_choice + ".mwrt"
            short_file_definition = (text_editor_choice[:20] + " . . .") if len(text_editor_choice) > 20 else text_editor_choice
            user_files[text_editor_file_name_choice] = {
                "short_content": short_file_definition,
                "full_content": text_editor_choice,
                "creation_time": file_creation_time
            }
            print(f"{Fore.CYAN}Write another text file? Type {Fore.GREEN}y/n{Style.RESET_ALL}")
            while True:
                write_another = input(f"{Fore.RED}> {Style.RESET_ALL}")
                if write_another == "y":
                    print(f"{Fore.BLUE}Write below . . .{Style.RESET_ALL}")
                    text_editor_input()
                    break
                elif write_another == "n":
                    desktop_menu()
                    break
                else:
                    print(f"{Fore.RED}Please type either y or n.{Style.RESET_ALL}")
        break


viewed_file = "none"


# FILE MANAGER --- CHANGE NAME FUNCTION
def change_name_file_manager_function():
    change_name_file_list = PrettyTable()
    change_name_file_list.field_names = [f"{Fore.YELLOW}Files{Style.RESET_ALL}"]
    for every_file_name in user_files:
        change_name_file_list.add_row([f"{Fore.YELLOW}{every_file_name}{Style.RESET_ALL}"])
    print(change_name_file_list)
    print(f"{Fore.YELLOW}Select a file to change the name of . . .{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}(type the name of the file without the extension. Type exit\\ to exit)")
    while True:
        change_name_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        full_file_name = change_name_choice + ".mwrt"
        if full_file_name in user_files:
            print(f"{Fore.YELLOW}Type the new name of file {Fore.CYAN}{change_name_choice}{Fore.YELLOW}. . .{Style.RESET_ALL}")
            while True:
                new_name_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
                if new_name_choice + ".mwrt" in user_files:
                    print(f"{Fore.RED}File name already exists! Please choose another name{Style.RESET_ALL}")
                else:
                    full_new_name = new_name_choice + ".mwrt"
                    user_files[full_new_name] = user_files[full_file_name]
                    del user_files[full_file_name]
                    print(f"{Fore.GREEN}File renamed successfully to {Fore.CYAN}{new_name_choice}{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}Do you want to change another file name? y/n")
                    while True:
                        change_another_name_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
                        if change_another_name_choice == "y":
                            change_name_file_manager_function()
                            break
                        elif change_another_name_choice == "n":
                            file_manager()
                            break
                        else:
                            print(f"{Fore.RED}That option doesn't exist! Please type either y or n{Style.RESET_ALL}")

        elif change_name_choice == "exit\\":
            file_manager()
            break

        else:
            print(f"{Fore.RED}That file doesn't exist! Make sure you're typing it without the extension!{Style.RESET_ALL}")


# FILE MANAGER --- DELETE A FILE FUNCTION
def delete_file_manager_function():
    delete_file_list = PrettyTable()
    delete_file_list.field_names = [f"{Fore.YELLOW}Files{Style.RESET_ALL}"]
    for file_name in user_files:
        delete_file_list.add_row([f"{Fore.YELLOW}{file_name}{Style.RESET_ALL}"])
    print(delete_file_list)
    print(f"{Fore.YELLOW}Select a file to {Fore.RED}delete {Fore.YELLOW}. . .{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}(type the name of the file without the extension. This action is permanent. Type exit\\ to exit){Style.RESET_ALL}")
    while True:
        delete_file_manager_function_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if delete_file_manager_function_choice + ".mwrt" in user_files:
            print(f"{Fore.YELLOW}Are you sure you want to permanently delete file {Fore.CYAN}{delete_file_manager_function_choice}{Style.RESET_ALL}{Fore.YELLOW}?y/n{Style.RESET_ALL}")
            while True:
                delete_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
                if delete_choice == "y":
                    del user_files[delete_file_manager_function_choice + ".mwrt"]
                    print(f"{Fore.GREEN}File {Fore.RED}deleted {Fore.GREEN}successfully.{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}Delete another file? y/n")
                    while True:
                        random_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
                        if random_choice == "y":
                            delete_file_manager_function()
                            break
                        elif random_choice == "n":
                            file_manager()
                            break
                        else:
                            print(f"{Fore.RED}Please type either y or n!{Style.RESET_ALL}")
                elif delete_choice == "n":
                    file_manager()
                    break
                else:
                    print(f"{Fore.RED}Please type either y or n!{Style.RESET_ALL}")

        elif delete_file_manager_function_choice == "exit\\":
            file_manager()
        else:
            print(f"{Fore.RED}That file doesn't exist! (make sure you don't enter the extension{Style.RESET_ALL}")


# FILE MANAGER
def file_manager():
    new_screen()
    file_manager_title = pyfiglet.figlet_format("File Manager")
    print(f"{Fore.YELLOW}{file_manager_title}{Style.RESET_ALL}")
    user_files_list = PrettyTable()
    user_files_list.field_names = [f"{Fore.YELLOW}File name{Style.RESET_ALL}", f"{Fore.YELLOW}File contents{Style.RESET_ALL}", f"{Fore.YELLOW}Time of creation{Style.RESET_ALL}"]
    for file_name, file_data in user_files.items():
        user_files_list.add_row([f"{Fore.YELLOW}{file_name}{Style.RESET_ALL}", f"{Fore.YELLOW}{file_data['short_content']}{Style.RESET_ALL}", f"{Fore.YELLOW}{file_data['creation_time']}{Style.RESET_ALL}"])
    print(user_files_list)
    print(f"{Fore.LIGHTBLACK_EX}(type a file name to view all of its contents. Type exit\\ to exit)")
    print(f"""{Fore.YELLOW}Commands:
    del --- delete a file
    cn --- change the name of a file
    {Style.RESET_ALL}""")
    while True:
        file_manager_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if file_manager_choice == "del":
            delete_file_manager_function()
            break
        elif file_manager_choice == "cn":
            change_name_file_manager_function()
            break
        elif file_manager_choice == "exit\\":
            desktop_menu()
            break
        elif file_manager_choice + ".mwrt" in user_files:
            viewed_file = file_manager_choice + ".mwrt"
            full_file = user_files[viewed_file]
            print(f"{Fore.YELLOW}File name: {Fore.CYAN}{viewed_file}{Style.RESET_ALL}\n")
            print(f"{Fore.YELLOW}File contents:\n{Fore.CYAN}{full_file['full_content']}{Style.RESET_ALL}\n")
            print(f"{Fore.YELLOW}Time of creation: {Fore.GREEN}{full_file['creation_time']}{Style.RESET_ALL}\n")
            while True:
                view_files_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
                if view_files_choice == "exit":
                    file_manager()
                    break
                else:
                    print(f"{Fore.RED}That's not a command! Type exit to go back to the File Manager{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}That's not a command!{Style.RESET_ALL}")


# TEXT EDITOR
def text_editor():
    new_screen()
    text_editor_title = pyfiglet.figlet_format("Text Editor")
    print(f"{Fore.CYAN}{text_editor_title}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Type any text down below and it will be saved in your files. Note that once you press enter, the file will be saved (access it in File Manager), Type exit\\ to exit Text Editor.")
    text_editor_input()


# DESKTOP MENU
def desktop_menu():
    new_screen()
    main_title = pyfiglet.figlet_format("miniOS 0.0.1")
    print(f"{Fore.MAGENTA}{main_title}{Style.RESET_ALL}")
    program_list = PrettyTable()
    program_list.field_names = [f"{Fore.GREEN}App{Style.RESET_ALL}", f"{Fore.LIGHTBLUE_EX}Command{Style.RESET_ALL}"]
    program_list.add_row([f"{Fore.GREEN}Text Editor{Style.RESET_ALL}", f"{Fore.LIGHTBLUE_EX}tw{Style.RESET_ALL}"])
    program_list.add_row([f"{Fore.GREEN}File Manager{Style.RESET_ALL}", f"{Fore.LIGHTBLUE_EX}fm{Style.RESET_ALL}"])
    program_list.add_row([f"{Fore.GREEN}To-do List{Style.RESET_ALL}", f"{Fore.LIGHTBLUE_EX}td{Style.RESET_ALL}"])
    program_list.add_row([f"{Fore.GREEN}Calculator{Style.RESET_ALL}", f"{Fore.LIGHTBLUE_EX}c{Style.RESET_ALL}"])
    program_list.add_row([f"{Fore.GREEN}Minigames{Style.RESET_ALL}", f"{Fore.LIGHTBLUE_EX}mg{Style.RESET_ALL}"])
    program_list.add_row([f"{Fore.GREEN}Video Player{Style.RESET_ALL}", f"{Fore.LIGHTBLUE_EX}vp{Style.RESET_ALL}"])
    program_list.add_row([f"{Fore.GREEN}MiniCustom{Style.RESET_ALL}", f"{Fore.LIGHTBLUE_EX}m{Style.RESET_ALL}"])
    print(program_list)
    print(f"{Fore.LIGHTBLACK_EX}(type exit in any program input screen to exit, type shutdown to close miniOS){Style.RESET_ALL}")
    while True:
        desktop_menu_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if desktop_menu_choice == "tw":
            text_editor()
            return
        elif desktop_menu_choice == "fm":
            file_manager()
            return
        elif desktop_menu_choice == "td":
            to_do_list()
            return
        elif desktop_menu_choice == "c":
            calculator()
            return
        elif desktop_menu_choice == "mg":
            minigames()
            return
        elif desktop_menu_choice == "vp":
            video_player()
            return
        elif desktop_menu_choice == "m":
            mini_custom()
            return
        elif desktop_menu_choice == "shutdown":
            shutdown()
            return
        else:
            print(f"{Fore.RED}That program/command doesn't exist!{Style.RESET_ALL}")


# BOOT SCREEN
def boot_screen():
    new_screen()
    print("miniOS version 0.0.1 --- penguinguy25")
    print("Boot command required . . .")
    while True:
        boot_screen_choice = input(f"{Fore.RED}> {Style.RESET_ALL}")
        if boot_screen_choice == "on":
            desktop_menu()
            return
        elif boot_screen_choice == "shutdown":
            shutdown()
            return
        else:
            print("Boot command invalid.")


# Program execution
boot_screen()
