lines = []
line = input()
first = -1
while line:
    lines.append(line)
    line = input()
for i in range(len(lines)):
    if "Все хорошо" in lines[i]:
        if first == -1:
            first = i
        else:
            second = i
for i in lines[second - 1:first:-1]:
    print(i)