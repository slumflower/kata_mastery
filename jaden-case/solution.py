def to_jaden_case(string):
    wordlist = string.split()
    newlist = []

    for word in wordlist:
        word = word[0].upper() + word[1:]
        newlist.append(word)
    
    return " ".join(newlist)
