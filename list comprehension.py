# 1. The odd number list entered by user and the odd number list entered by me.
a=int(input("Enter an odd number: "))
b=int(input("Enter another odd number: "))
c=int(input("Enter another odd number(This is the last time- I swear!): "))
the_list=[a,b,c]
print("The list of odd numbers, entered at the USER'S INPUT is:",the_list)
the_my_list=[1,3,5,7,9]
print("The list of odd numbers, entered at MY INPUT is:",the_my_list)

# 2. The list of fruits, which I converted the first letter of every element to capital and then created the a new list, which contains the first letter of every element of the list as a capital letter.
fruits=['apple','banana','cherry','blackberry','mango']
print("The original list of fruits is:",fruits)
new_fruits=[fruit.capitalize() for fruit in fruits]
print("The list of fruits with the first letter of every element as a capital letter is:",new_fruits)
