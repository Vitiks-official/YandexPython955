n = int(input())
k = 2
some_n = 2
while n != 0:
    some_n = k
    while some_n % 2 == 0:
        some_n //= 2
    while some_n % 3 == 0:
        some_n //= 3
    while some_n % 5 == 0:
        some_n //= 5
    if some_n == 1:
        m = k
        n -= 1
    k += 1
print(m)