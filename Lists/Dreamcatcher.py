dreams = []
line = input()
while line:
    dreams.append(line)
    line = input()
maxd = ""
for i in dreams[int(input()) - 1:int(input())]:
    if len(i) > len(maxd):
        maxd = i
print(maxd)