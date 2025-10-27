n = int(input())
arr = []
for i in range(n + 1):
    arr.append(input())
word = arr[-1]
arr.sort()
for j in range(len(arr)):
    if arr[j] == word:
        ind = j
print(ind)