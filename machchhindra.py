import random

winning_number = random.randint(1,100)

guess =1

name=input("Enter your  name please: ")

number=int(input("Enter the number between 1 and 100: "))

game_over=False

while not game_over:


    if number==winning_number:

        print(f"Congractulations {name} you win...!!!")

        print(f"{name} you guessed this number in {guess} time")

        game_over=True

    else:

        if number < winning_number:

            print("Two low")

        else:

            print("To high")

        guess += 1

        number=int(input("Guess Again..."))
