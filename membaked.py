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

def guess(beginning):
    # get all words that match
    matches = [word for word in words.keys() if word.startswith(beginning)]

    # get the first four letters of all of them
    subs = {}
    for match in matches:
        if match[0:4] in subs:
            subs[match[0:4]] += 1
        else:
            subs[match[0:4]] = 1
    return subs

inp = input("mbb$> ")
while inp != "quit" and inp != "exit":
    args = inp.split(" ")
    args = args[1:len(args)]
    if inp.startswith("guessfl "): # Guess By Word
        best = sorted(guess(args[0]).items(), key=lambda x:x[1])
        best.reverse()
        for (k,v) in best:
            print(f"{k}: {v}")
    elif inp.startswith("guess "): # extend the word
        length = -1;
        if len(args) > 1 and args[1]:
            length = int(args[1])
        out = ""
        for word in words.keys():
            if word.startswith(args[0]) and (length == -1 or len(word) == length):
                out += word + "\n"
        if out == "":
            out = "No matches."
        print(out)
    elif inp.startswith("define "):
        for arg in args:
            if arg in words:
                print(words[arg])
            else:
                print("Not a membean word. You should modify it to include this word if this is a mistake.")
    elif inp.startswith("guesstl "): # Guess By Letters
        best = guess(args[0]).keys()
        filtrs = {}
        scltrs = {}
        # for every 3rd letter
        for word in best:
            letter = word[len(args[0])]
            if letter in filtrs:
                filtrs[letter] += 1
            else:
                filtrs[letter] = 1
            letter = word[len(args[0])+1]
            if letter in scltrs:
                scltrs[letter] += 1
            else:
                scltrs[letter] = 1
        key = lambda x:x[1]
        print(sorted(filtrs.items(), key=key))
        print(sorted(scltrs.items(), key=key))
    elif inp.startswith("trim "):
        matches = []
        wordkeys = words.keys()
        wordtotrim = args[0]
        for word in wordkeys:
            if wordtotrim.startswith(word) or wordtotrim.endswith(word):
                matches.append(word)
        
        if len(matches) == 0:
            print("No matches.")
        else:
            print("Matches found:")
            for word in matches:
                print(f"{word}")
    elif inp.startswith("help"): # help
        print("quit      : quit program")
        print("exit      : quit program")
        print("guessfl <arg> : guess by most common first four letters.")
        print("guesstl <arg> : guess most likely two letters to go next.")
        print("define <arg(s)> : define a word, if its in the dict")
        print("guess <arg> <?len> : extend any set of letters to display any matching words")
        print("help       : display this menu")
        print("trim <arg> : trims the word to remove suffixes")
    inp = input("mbb$> ")
