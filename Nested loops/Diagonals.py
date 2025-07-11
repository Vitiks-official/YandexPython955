symb = input()
n = int(input())
for i in range(n):
    line = ""
    for j in range(n):
        if j == i or j == n - i - 1:
            line += f"{symb} "
        else:
            line += "  "
    print(line)