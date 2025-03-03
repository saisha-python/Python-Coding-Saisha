import random
playing=True
number=str(random.randint(10,20))
print("Welcome to the Number Game!")
print("You have to guess a number from 0 to 9.")
print("Your game will end when you guess the correct number.")
print("Good Luck!")
while playing:
    guess=input("Enter your guess: \n")
    if guess==number:
        print("Congratulations! You guessed the correct number.")
        print("Game Over!")
        print("The Number was, ",number)
        break
    else:
        print("Incorrect guess. Try again.\n")