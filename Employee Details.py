class RandomPerson(object):
    def __init__(self, name, idcardno):
        self.name = name
        self.idcardno = idcardno
    def display(self):
        print(self.name)
        print(self.idcardno)
class Employee(RandomPerson):
    def __init__(self, name, idcardno, salary, post):
        self.salary = salary
        self.post = post
        RandomPerson.__init__(self, name, idcardno)
a= Employee("MsVireetha", 8837629383, 2000000, "Owner Of Amazing Company" )
a.display()