sh = input()
line = input()
gl = 'ауоыиэяюеё'
sgl = 'бвгджзйклмнпрстфхцчшщ'
nothing = True
while line != "":
    crct = True
    if "*" in sh:
        crct = len(line) >= len(sh) - 1
        if len(line) >= len(sh) - 1:
            for i in range(len(sh[:sh.find("*")])):
                if sh[i] == "0":
                    if line[i] not in gl:
                        crct = False
                        break
                if sh[i] == "1":
                    if line[i] in gl:
                        crct = False
                        break
            for i in range(len(sh[sh.find("*") + 1:])):
                if sh[-i - 1] == "0":
                    if line[-i - 1] not in gl:
                        crct = False
                        break
                if sh[-i - 1] == "1":
                    if line[-i - 1] in gl:
                        crct = False
                        break
    else:
        crct = len(line) == len(sh)
        if len(line) == len(sh):
            for i in range(len(sh)):
                if sh[i] == "0":
                    if line[i] not in gl:
                        crct = False
                        break
                if sh[i] == "1":
                    if line[i] in gl:
                        crct = False
                        break
    if crct:
        nothing = False
        print(line)
    line = input()
if nothing:
    print("Есть нечего, значить!")
