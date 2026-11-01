import random
import math

def format():
    print(line_breaker)
    print(signal)
    print(line_breaker)

signal = "You have entered a new program"
line_breaker = "-" * 40

sign_list = ["Star" , "Clover" , "Greek Evil Eye" , "Rose"]

print(line_breaker)
print("-" * 8 , "RANDOM GAME CALCULATOR" , "-" * 8)
print(line_breaker)

lucky_number = random.randint(1,1000)
lucky_sign = random.choice(sign_list)

print(f"Your lucky number - {lucky_number}")
print(f"Your lucky sign - {lucky_sign}")


user_choices = ["Play PS5" , "Play football" , "Play Monopoly" , "Read a book"]
rand_user_choices = random.choice(user_choices)
print(f"Your activity for today - {rand_user_choices}")

format()

print("-" * 39)
print("-" * 11 , "THE ROPASC GAME" , "-" * 11)
print("-" * 39)
print("Your game - Rock, Paper, Scissors")

def game():

    list = ["rock", "paper", "scissors"]

    while True:

        print("What is your choice:")
        print(line_breaker)
        print("Rock")
        print("Paper")
        print("Scissors")
        print(line_breaker)

        user_choice = input().lower()

        if user_choice not in list:
            print("INVALID INPUT")
            break

        compu_choice = random.choice(list)
            
        print(line_breaker)
        print(f"The computer's choice was - {compu_choice}. Your choice was - {user_choice}.")
        print(line_breaker)

        won_result = "YOU WON"
        loss_result = "YOU LOST"
        draw_result = "IT'S  DRAW"

        if user_choice == compu_choice:
            print(draw_result)

        elif (user_choice == "paper" and compu_choice == "rock") or (user_choice == "scissors" and compu_choice == "paper") or (user_choice == "rock" and compu_choice == "scissors"):
            print(won_result)

        else:
            print(loss_result)

        print(line_breaker)
        user_continue = input("Do you want to continue? (Y/N)").lower()
        if user_continue == "n" :
            print("You have exited this game.")
            break

game()   

try:
    format()

    user_decimal = float(input("Please enter your chosen decimal: "))
    ceil_val = math.ceil(user_decimal)
    floor_val = math.floor(user_decimal)

    print(f"The ceiling of your decimal number - {ceil_val}")
    print(f"The floor of your decimal number - {floor_val}")

except ValueError:
    print("This is not a decimal. Please try again")

except:
    print("This has given an error. Please try again")

try:
    format()

    number_1 = 17
    number_2 = -10
    print(f"The first number - {number_1}")
    print(f"The number to change the sign {number_2}")
    print("Copy sign result:", math.copysign(number_1, number_2))

except ValueError:
    print("This is not a decimal. Please try again")

except:
    print("This has given an error. Please try again")

try:
    format()

    negative_number = int(input("Enter a negative number: "))
    print("Absolute value: ", math.fabs(negative_number))

except ValueError:
    print("This is not a decimal. Please try again")

except:
    print("This has given an error. Please try again")

try:
    format()

    num1 = int(input("Enter first number for GCD: "))
    num2 = int(input("Enter second number for GCD: "))
    print("GCD is:", math.gcd(num1, num2))

except ValueError:
    print("This is not a decimal. Please try again")

except:
    print("This has given an error. Please try again")

    format()

    print("-" * 8 , "RANDOM GAME CALCULATOR" , "-" * 8)
    print("Random Activity:", rand_user_choices)
    print("Lucky Number:", lucky_number)
    print("Lucky Sign:", lucky_sign)
    print(line_breaker)