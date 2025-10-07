alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
for i in range(4):
    print(alp[(n - 1 + i) % len(alp)], end="")