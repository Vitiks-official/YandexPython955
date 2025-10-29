nw = ""
for i in range(int(input())):
    word = input()
    if len(word) < i + 1:
        nw = "None"
        break
    nw += word[-i - 1]
print(nw)