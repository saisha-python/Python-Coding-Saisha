
import random
class FruitQuiz:
    def __init__(self):
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'banana':'yellow',
                     'watermelon':'green',
                     'banana':'yellow',}
    def quiz(self):
        while(True):
            fruit, color= random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            answer=input()
            if(answer.lower() == color):
                print("Correct!")
            else:
                print("Incorrect! The correct answer is {}".format(color))
            options=input("Do you want to continue? (yes/no): ")
            if (options):
                break
print("Welcome to the Fruit Quiz!")
fq=FruitQuiz()
fq.quiz()
# Compare this snippet from flashcards.py: