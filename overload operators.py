class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self, other):
        if(self.a < other.a):
            return "Object 1 is less than Object 2"
        else:
            return "Object 2 is less than Object 1"
    def __eq__(self, other):
        if(self.a==other.a):
            return "Both are equal"
ob1=A(2)
ob2=A(3)
print("Passed values", ob1.a, ob2.a)
print(ob1<ob2)
ob3=A(4)
ob4=A(4)
print("Passed values", ob3.a, ob4.a)
print(ob3==ob4)