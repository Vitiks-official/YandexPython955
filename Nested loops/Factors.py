n = int(input())
st = f"{n} = "
for i in range(2, n + 1):
    while n % i == 0:
        n //= i
        st += f"{i}"
        if n != 1:
            st += " * "
print(st)