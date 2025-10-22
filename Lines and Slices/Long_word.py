line = input() + " "
l = 0
pos = 0
maxl = 0
for i in range(len(line)):
    if line[i] == " ":
        if maxl < l:
            maxl = l
            pos = i - l
        l = 0
    else:
        l += 1
print(line[pos:maxl + pos])