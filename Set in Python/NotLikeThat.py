answer = set()
letter = input()
for i in range(int(input())):
    word = input()
    if len(set(word) - set(letter)) > len(answer):
        answer = set(word) - set(letter)
if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i, end="")