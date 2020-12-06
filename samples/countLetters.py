
def countLetters(text: str):
    d = dict()
    for char in text:
        if d.get(char) == None:
            d[char] = 1
        else:
            d[char] += 1

    for i in d:
        print(i + ": " + str(d[i]))

countLetters("here are some letters")

