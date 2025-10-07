num = input()
max_p = int(num[0]) * int(num[1]) * int(num[2]) * int(num[3]) * int(num[4])
for i in range(len(num) - 4):
    max_p = max(max_p, int(num[i]) * int(num[i + 1]) * int(num[i + 2]) * int(num[i + 3]) * int(num[i + 4]))
print(max_p)