num1=float(input("Please Enter the First Value:"))
num2=float(input("Please Enter the Second Value:"))
while(num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp
gcf=num1
print("GCF of the two numbers in:", gcf)