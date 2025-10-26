letter = input()
line = input()
first = -1
last = len(line)
for i in range(len(line)):
    if line[i] == letter:
        if first == -1:
            first = i
        else:
            last = i
print(line[first + 1:last])