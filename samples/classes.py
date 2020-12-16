x = 5
class NotePad:
    x = 5
    thingsToRemember = []
    def __init__(self):
        #print("Calling __init__")
        "nothing"
    def remember(self, text):
        self.thingsToRemember.append(text)
    def look(self):
        for i in self.thingsToRemember:
            print(i)
    def count(self):
        return len(self.thingsToRemember)
    def five():
        return NotePad.x 
    def myfive(self):
        return self.x
    def bump():
        NotePad.x += 1

def main():
    
    notepad = NotePad()
    notepad.remember("Movie: Forrest Gump")
    notepad.remember("Music: Smooth jazz")
    notepad.x = 6
    print(notepad.myfive())

    notepad2 = NotePad()
    notepad2.remember("Nevermind")
    print(notepad2.myfive())

    NotePad.bump()
    print(NotePad.five())

    # Q: write a class NumberHelper to remember some numbers (integers)
    #   Methods:
    #       numbers()  returns a list of the numbers (sorted)
    #       toString() returns a string of all the numbers (sorted) separated by spaces  
    #       min()      returns the smallest number in the list
    #       max()      returns the largest number in the list
    #       mean()     return the mean of the numbers
    #       median()   return the median of the numbers
    #       mode()     return the mode of the numbers
main()
