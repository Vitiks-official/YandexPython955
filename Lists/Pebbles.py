nums = [int(input()) for i in range(int(input()))]
new_nums = []
for i in nums:
    if i % 2 == sum(nums) % 2:
        new_nums.append(i)
print(sum(nums) - sum(new_nums), new_nums)