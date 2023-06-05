from replit import clear
from art import logo 
import sys

print(logo)

# Functions that calculate with the user numbers
def plus(num_one, num_two):
    return num_one + num_two


def minus(num_one, num_two):
    return num_one - num_two


def multiply(num_one, num_two):
    return num_one * num_two


def divide(num_one, num_two):
    return num_one / num_two

# dictionary used for run the calculation functions with users option
dic = {
    "+": plus,
    "-": minus,
    "*": multiply,
    "/": divide,
}


# calculates all next operation chosen by user
def calculator(answer):
    print(logo)
    next_run = True
    while next_run:
        next_operation = input("\n +   -   *   /  \n\n Choose the operation: ")
        third_num = float(input("Choose the number: "))
        calc_func = dic[next_operation]
        answer_two = calc_func(answer, third_num)
        clear()
        print(f"{answer} {operation} {third_num} = {answer_two}\n")
        next = input("Next calculation? Type 'y' or 'n' ")
        if next == "y":
            clear()
            calculator(answer=answer_two)
        elif next == "n":
            sys.exit("Thank you Bye!")
            
# variable used to run the while loop and run the program 
running = True
# first shown window. it calculates with first numbers
while running:
    first_num = float(input(" What's your number: "))
    operation = input(" \n +   -   *   /  \n\n Pick an operation: ")
    second_num = float(input(" What's the next number: "))
    calc_func = dic[operation]
    answer = calc_func(first_num, second_num)
    print(f"\n{first_num} {operation} {second_num} = {answer}")
    next_calc = input( "\n Type: \n\n next - next calculation\n new - new calculatrion\n exit - exit program \n"
    )
    clear()
    # if users choose 'next' then the program will run the next calculation function
    if next_calc == "next":
        calculator(answer)
        running = False
# it changes variable to false and exits the program
    elif next_calc == "exit":
        sys.exit("Thank you Bye")
