all_colors = set()
more2 = set()
k = 0
for i in range(int(input())):
    for j in range(int(input())):
        color = input()
        if color in all_colors:
            more2.add(color)
            k += 1
        all_colors.add(color)
print(len(more2), k + len(more2))