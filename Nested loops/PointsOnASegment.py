x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = abs(x2 - x1)
y = abs(y2 - y1)
while y != 0 and x != 0:
    if x > y:
        x %= y
    else:
        y %= x
print(x + y + 1)