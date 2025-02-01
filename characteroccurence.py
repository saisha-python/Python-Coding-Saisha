string=input("Please enter your own word:")
char= input("Please enter your own character:")
i=0
count=0
while i<len(string):
    if string[i]==char:
        count+=1
    i+=1
print("The total number of occurence of",char,"is:",count)