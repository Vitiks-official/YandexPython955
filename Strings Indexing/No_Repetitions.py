line = input()
while line != "":
    if len(set(line)) == len(line):
        print(line)
    line = input()