num = int(input())
for i in range(1, num + 1):
    for j in range(1, i + 1):
        if i * j == num:
            print(i, j)