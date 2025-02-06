print("Here are some ways to earn brownie points: ")
print("1.kiwi")
print("2.avoiding sweets")
print("3.eating healthy")
print("4.exercising")
print("5.other")
earning=str(input("How did you earn brownie points? "))
if earning == "kiwi":
    print("You've earned 10 brownie points today!")
if earning == "avoiding sweets":
    print("You've earned 10 brownie points today!")
if earning == "eating healthy":
    print("You've earned 5 brownie points today!")
if earning == "exercising":
    print("You've earned 5 brownie points today!")
if earning == "other":
    print("Check in with your parent or guardian to see how many brownie points you've earned today!")
elif earning != "kiwi" and earning != "avoiding sweets" and earning != "eating healthy" and earning != "exercising" and earning != "other":
    print("Sorry, that's not a way to earn brownie points. Try again!")