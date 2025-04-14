class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__ (self):
        return self.word+"("+self.meaning+")"

flash =[]
print("welcme to the flashcard game.")
while(True):
    word = input("enter the word you want to add to flashcard : ")
    meaning = input("enter the meaning of word you want to add to flashcard : ")
    flash.append(flashcard(word,meaning))
    option = int(input("enter 0 to add another flashcard / otherwise enter 1 : "))
    if(option):
        break
print("n Your Flashcards")
for i in flash:
    print(">",i)