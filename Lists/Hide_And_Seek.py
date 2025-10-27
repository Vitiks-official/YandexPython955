n = int(input())
arr = []
for i in range(n):
    line = input()
    arr.append(line)
for i in range(int(input())):
    word = input()
    for j in range(len(arr) + 1):
        if j == len(arr):
            print(-1)
        elif word in arr[j]:
            print(j + 1)
            break