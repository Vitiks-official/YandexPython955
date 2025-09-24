first = set()
second = set()
for i in range(int(input())):
    first.add(int(input()))
for i in range(int(input())):
    second.add(int(input()))
for i in first & second:
    print(i)