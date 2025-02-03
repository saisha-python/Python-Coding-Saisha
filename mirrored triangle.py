hey=str(input("Enter your name: "))
print("Hey",hey,"!")
print("Let's make a mirrored triangle!")
def awesomepie_triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '^' * i)
n = 5
awesomepie_triangle(n)
print("OK, so u have the mirrored triangle!")
print("Bye",hey,"!")