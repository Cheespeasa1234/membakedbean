# DEPENDENCIES
from tkinter import *

words = {}
file1 = open('words.txt', 'r')
lines = file1.readlines()

# PROCESS FILE
for line_ind in list(range(len(lines))):
    line = lines[line_ind]
    if line.count(":") > 0:
        # this is a definition
        tokens = line.split(":")
        words[tokens[0]] = tokens[1].strip()

# get starting matches
def guess(beginning):
    matches = []
    for word in words.keys():
        if word.startswith(beginning):
            matches.append(word)

    # get third letters
    third_letters = {}
    for match in matches:
        letter = match[2]
        if letter in third_letters.keys():
            third_letters[letter] += 1
        else:
            third_letters[letter] = 1

    # get most common third letter
    max = 0
    best_third = ""
    for letter in third_letters.keys():
        if third_letters[letter] > max:
            max = third_letters[letter]
            best_third = letter

    # get fourth letters
    fourth_letters = {}
    for match in matches:
        letter = match[3]
        if letter in fourth_letters.keys():
            fourth_letters[letter] += 1
        else:
            fourth_letters[letter] = 1

    # get most common fourth letter
    max = 0
    best_fourth = ""
    for letter in fourth_letters.keys():
        if fourth_letters[letter] > max:
            max = fourth_letters[letter]
            best_fourth = letter

    return f'{beginning}{best_third}{best_fourth}'


# GUI
m = Tk()
m.geometry('300x400')
m.title("Membaked")
button = Button(m, text="Exit", width="25", command=m.destroy)
button.place(relx = 0.25, rely = 0.5)
'''
widgets are added here
'''
m.mainloop()
