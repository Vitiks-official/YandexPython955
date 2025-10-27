n = int(input())
m = int(input())
words = [input() for i in range(n)]
lines = [input() for i in range(m)]
flag = True
for i in lines:
    step = ""
    for j in i:
        if j.isdigit():
            step += j
    step = int(step)
    if i[step - 1::step] in words:
        print(i[step - 1::step])
        words.remove(i[step - 1::step])
        flag = False
if flag:
    print("NO")

