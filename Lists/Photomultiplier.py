m = int(input())
nums = sorted([int(input()) for i in range(int(input()))])[::-1]
n1, n2 = 0, 0
best = [-1] * m
for i in nums:
    need = (m - i % m) % m
    if best[need] != -1 and n1 * n2 < i * best[need]:
        n1, n2 = best[need], i
    if best[i % m] == -1 or best[i % m] < i:
        best[i % m] = i
print(n2, n1)
