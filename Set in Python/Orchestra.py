first, second, third = set(), set(), set()
sn = input()
while sn != "":
    first.add(sn)
    sn = input()
sn = input()
while sn != "":
    second.add(sn)
    sn = input()
sn = input()
while sn != "":
    third.add(sn)
    sn = input()
some = (first | second | third) - ((first & second) | (third & second) | (first & third))
for i in some:
    print(i)
