class Ms_Vireetha:
    def __init__(self):
        print("Ms. Vireetha's class is created.")
    def __del__(self):
        print("Ms. Vireetha's class is deleted.")
def Create_object():
    print("Creating an object of Ms. Vireetha's class.")
    obj=Ms_Vireetha()
    print("Function is executed and ended.")
    return obj
print('Calling the Create_object function.')
obj=Create_object()
print("Ms. Vireetha's program is ended.")