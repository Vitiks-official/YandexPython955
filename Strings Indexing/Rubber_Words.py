word = input()
if len(word) % 2:
    first = word[:len(word) // 2]
    second = word[len(word) // 2 + 1:]
    print(len(first) * " " + word[len(word) // 2])
    for i in range(len(first)):
        print(" " * (len(first) - 1 - i) + first[-i - 1] + " " * (i * 2 + 1) + second[i])
else:
    first = word[:len(word) // 2]
    second = word[len(word) // 2:]
    for i in range(len(first)):
        print(" " * (len(first) - 1 - i) + first[-i - 1] + " " * i * 2 + second[i])