class Parrot:
    species="avian"
    def __init__(self, name, age):
        self.name=name
        self.age=age
class Wolf:
    species="canine"
    def __init__(self, name, age):
        self.name=name
        self.age=age
blu=Parrot("Blu", 5)
Cutie=Wolf("Cutie", 3)
print("Animal #1 at the Sharma Family Animal Sanctuary's name is {}".format(blu.name))
print("Blu is a {}".format(blu.species))
print("Blu's age is {}".format(blu.age))
print("Animal #2 at the Sharma Family Animal Santcuary's name is {}".format(Cutie.name))
print("Cutie is a {}".format(Cutie.species))
print("Cutie's age is {}".format(Cutie.age))