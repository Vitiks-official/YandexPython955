first, second, third = set(), set(), set()
answer = set()
i = 0
while i < 3:
    num = input()
    if i == 0:
        first.add(num)
    if i == 1:
        second.add(num)
    if i == 2:
        first.add(num)
    if num == "":
        i += 1
for i in range(int(input())):
    num = input()
    if num in first | second | third:
        answer.add(num)
for i in answer:
    print(i)