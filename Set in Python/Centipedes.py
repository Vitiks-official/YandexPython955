first, second, third = set(), set(), set()
for i in range(int(input())):
    num = int(input())
    if num > 40:
        first.add(num)
    if num % 2 == 0:
        second.add(num)
    if num % 3 == 0:
        third.add(num)
print(*(((first & second) | (third & second) | (first & third)) - (first & second & third)))