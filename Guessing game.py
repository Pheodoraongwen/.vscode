import random

name = input("Hello! What is your name? ")
print(f"Welcome {name} to the Number Guessing Game!")

play_again = "yes"
while play_again == "yes":
    try:
        level = input("Choose a level: Easy, Medium, or Hard: ").lower()

    except ValueError:
        print("Invalid input. Please enter a valid level.")
        continue

    if level == "easy":
        print("You have 5 trials to guess the number between 1 and 10")
        number = random.randint(1, 10)
    elif level == "medium":
        print("You have 5 trials to guess the number between 1 and 50")
        number = random.randint(1, 50)
    elif level == "hard":
        print("You have 5 trials to guess the number between 1 and 100")
        number = random.randint(1, 100)
    else:
        print("Invalid level. Please choose Easy, Medium, or Hard.")
        continue

    trials = 0

    while trials < 5:

        guess = int(input("Take a guess: "))

        if guess == number:
            print(f"Congratulations {name}! You got it right! 🎉")
            print(f"You have used {trials + 1} trials to guess the number.")
            break
        else:
            print("Oops! Wrong guess.")
            if guess > number:
                print("Your guess is way too high")
            elif guess < number:
                print("Your guess is way too low")
            trials += 1

            if trials == 5:
                print("Oops! Your trials are over")
                print(f"The correct number was {number}")

    play_again = input("Do you want to play again? (yes/no): ").lower()