line = input()
pos = -1
for i in range(len(line)):
    if line[i] == "-":
        pos = i
print(line[pos + 1:] + "-" + line[:pos])