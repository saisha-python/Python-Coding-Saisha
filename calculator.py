def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def mul(p,q):
    return p*q
def div(p,q):
    return p/q
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=input("Enter choice(1/2/3/4):")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",mul(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("Invalid input")