lines = [input() for i in range(int(input()))]
words = [input() for i in range(int(input()))]
for i in lines:
    if all([j in i for j in words]):
        print(i)