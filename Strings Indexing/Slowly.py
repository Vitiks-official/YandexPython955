line = input()
nl = ""
for i in range(len(line)):
    nl += (i + 1) * line[i]
print(nl)