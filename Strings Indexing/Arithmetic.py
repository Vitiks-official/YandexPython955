line = input()
answer = int(line[0])
for i in range(1, len(line), 2):
    if line[i] == "+":
        answer += int(line[i + 1])
    else:
        answer -= int(line[i + 1])
print(answer)