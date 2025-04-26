class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+ '(' + self.meaning + ')'
flash=[]
print("Welcome, ladies and gentlmen, to the world's greatest show, on the face of the earth, or wherever you go!")
print("The...(drumroll please)... Flashcard App!")
while(True):
    word=input("Enter the thing you wanna add to the flashcard: ")
    meaning=input("Enter the meaning of the thing you wanna add to the flashcard: ")
    flash.append(flashcard(word, meaning))
    next_option=input("Do you want to add another flashcard? (yes/no): ")
    if(next_option):
        break
print("Your flashcards are:")
for i in flash:
    print(">",i)