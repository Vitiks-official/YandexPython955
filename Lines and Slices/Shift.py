line1 = input()
line2 = input()
if len(line1) == len(line2):
    for i in range(len(line1) + 1):
        if line1 == line2:
            print(i)
            break
        line2 = line2[1:] + line2[0]
else:
    print("NO")