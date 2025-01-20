medical_cause=input("Did you have a medical cause Y or N:")
atten=int(input("Enter the attendance number of the student:"))
if medical_cause=='Y':
    print("You are eligible")
else:
    if atten>=75:
        print("You are eligible")
    else:
        print("You are not eligible")