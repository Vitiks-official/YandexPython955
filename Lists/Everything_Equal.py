line = input()
words = []
maxl = 0
while line:
    words.append(line)
    maxl = max(maxl, len(line))
    line = input()
for i in words[::-1]:
    k = maxl - len(i)
    if k % 2:
        print("-" * (k // 2) + i + "-" * (k // 2 + 1))
    else:
        print("-" * (k // 2) + i + "-" * (k // 2))