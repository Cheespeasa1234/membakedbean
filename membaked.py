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
while inp != "qwt":
    args = inp.split(" ")
    args = args[1:len(args)]
    if inp.startswith("gbw"): # Guess By Word
        best = sorted(guess(args[0]).items(), key=lambda x:x[1])
        best.reverse()
        for (k,v) in best:
            print(f"{k}: {v}")
    elif inp.startswith("ext"): # extend the word
        out = ""
        for word in words.keys():
            if word.startswith(args[0]):
                out += word + "\n"
        if out == "":
            out = "No matches."
        print(out)
    elif inp.startswith("def"):
        if args[0] in words:
            print(words[args[0]])
        else:
            print("Not a membean word. You should modify it to include this word if this is a mistake.")
    elif inp.startswith("gbl"): # Guess By Letters
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
    elif inp.startswith("trm"):
        inp = args[0]
        out = ""
        for word in words:
            if str(word).startswith(inp) or str(word).endswith(inp):
                out += word + "\n"

        if out == "":
            print("No matches found.")
        else:
            print("Matches:\n" + out)
    elif inp.startswith("hlp"): # help
        print("qwt       : quit program")
        print("gbw <arg> : guess by most common first four letters.")
        print("gbl <arg> : guess most likely two letters to go next.")
        print("def <arg> : define a word, if its in the dict")
        print("ext <arg> : extend any set of letters to display any matching words")
        print("hlp       : display this menu")
        print("trm <arg> : trims the word to remove suffixes")
    inp = input("mbb$> ")
