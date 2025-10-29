letter = input()
if ord(letter) < ord("a"):
    print(chr(ord(letter) + 32))
else:
    print(chr(ord(letter) - 32))