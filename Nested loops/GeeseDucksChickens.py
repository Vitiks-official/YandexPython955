n = int(input())
m = int(input())
for i in range(0, n + 1):
    for j in range(0, n + 1 - i):
        for k in range(0, n + 1 - i - j):
            if i * 25 + j * 10 + k * 7 == m and i + j + k == n:
                print(i, j, k)