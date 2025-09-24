first = set(input())
second = set(input())
third = set(input())
answer = (first & second) | (third & second) | (first & third)
for i in answer:
    print(i, end="")

