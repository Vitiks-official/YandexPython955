line = input() + " "
word = ""
for i in line:
    if i == " ":
        print(word)
        word = ""
    else:
        word += i

