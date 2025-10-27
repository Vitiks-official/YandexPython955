clrs = [input() for i in range(int(input()))]
for i in range(int(input())):
    print(clrs[i % len(clrs)])