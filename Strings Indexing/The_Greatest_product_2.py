num = input()
step = int(input())
maxa = 0
for i in range(len(num) - step + 1):
    answer = 1
    for j in range(i, i + step):
        answer *= int(num[j])
    maxa = max(maxa, answer)
print(maxa)