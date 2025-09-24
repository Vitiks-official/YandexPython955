allf = set()
everyf = set()

for i in range(int(input())):
    f = input()
    allf |= set(f)
    if i == 0:
        everyf = set(f)
    else:
        everyf &= set(f)
print(len(everyf), len(allf))
