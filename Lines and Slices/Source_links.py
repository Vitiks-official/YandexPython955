line = input()
open_pos = 0
count = 0
i = 0
while i < len(line):
    if line[i] == "[":
        if count == 0:
            open_pos = i
        count += 1
    elif line[i] == "]":
        count -= 1
        if count == 0:
            line = line[:open_pos] + line[i + 1:]
            i = 0
    i += 1
print(line)
