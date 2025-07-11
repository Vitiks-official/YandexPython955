x = int(input())
y = int(input())
r = int(input())
count = 0
for i in range(x - r, x + r + 1):
    for j in range(y - r, y + r + 1):
        if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
            count += 1
print(count)