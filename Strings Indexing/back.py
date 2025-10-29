word = input()
first = word[0]
second = word[len(word) // 2]
third = word[-2]
fourth = word[-1]
for i in [first, second, third, fourth]:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ord(i) - 3 < 65:
            print(chr(ord(i) + 23), end="")
        else:
            print(chr(ord(i) - 3), end="")
    else:
        if ord(i) - 3 < 97:
            print(chr(ord(i) + 23), end="")
        else:
            print(chr(ord(i) - 3), end="")