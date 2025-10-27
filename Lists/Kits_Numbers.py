num = int(input())
nums = list(map(int, list(str(num))))
step = len(nums)
while num > nums[-1]:
    nums.append(sum(nums[-step:]))
if nums[-1] == num:
    for i in nums:
        print(i, end=" ")
else:
    print("NO")