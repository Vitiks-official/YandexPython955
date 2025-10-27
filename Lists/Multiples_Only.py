n = int(input())
nums = []
while n != 0:
    nums.append(n)
    n = int(input())
print([i for i in nums if i % len(nums) == 0])