word = input()
nw = ''
if len(word) % 2 == 0:
    for i in range(len(word) // 2):
        nw += word[i] + word[i + len(word) // 2]
    print(nw)
else:
    for i in range(len(word) // 2):
        nw += word[i] + word[i + len(word) // 2 + 1]
    print(nw + word[len(word) // 2])