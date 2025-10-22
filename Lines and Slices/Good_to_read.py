line = input()
first, second = -1, -1
for i in range(len(line)):
    if line[i] in "ESM":
        if first == -1:
            first = i
        elif second == -1:
            second = i
print(first + 1)
print(second - first - 1 if second != -1 else len(line) if first == -1 else len(line) - first - 1)
print(len(set(line) - set("ESM ")))