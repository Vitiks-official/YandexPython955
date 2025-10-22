line = input()
step = int(input())
i = True
while line:
    if i:
        print(line[-step:])
        i = not i
        line = line[:-step]
    else:
        print(line[:step])
        i = not i
        line = line[step:]