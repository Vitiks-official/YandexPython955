s = int(input())
e = int(input())
step = int(input())
for i in range(s, e + 1, step):
    for j in range(s, e + 1, step):
        print(f"{i} + {j} = {i + j}", end="\t")
    print("")