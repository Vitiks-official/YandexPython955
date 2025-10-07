line = input()
answer = "(:_0_:)"
for i in range(len(line) - 1):
    if ord(line[i]) > ord(line[i + 1]):
        answer = line[i + 1]
        break
print(answer)