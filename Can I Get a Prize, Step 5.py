brownie=int(input("How many brownie points did you earn this week so far? Enter a number: "))
if brownie >=50 and brownie <=100:
    print("You can get a prize... a sweet treat!")
elif brownie <=50:
    print("You can't get a prize, but you can try again tomorrow!")
if brownie >=100:
    print("You can get a prize... a small toy!")