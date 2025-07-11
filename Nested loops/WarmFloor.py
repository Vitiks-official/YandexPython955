n = int(input())
m = int(input())
if m > n:
    m, n = n, m
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i % 2 == 0:
            print(n * i - j + 1, end="\t")
        else:
            print(n * (i - 1) + j, end="\t")
    print()