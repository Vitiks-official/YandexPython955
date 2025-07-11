n = int(input())
count = 0
while n > 0:
    while n > 7:
        if n % 8 == 7:
            count += 1
        n //= 8
    if n == 7:
        count += 1
    n = int(input())
print(count)