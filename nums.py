num = input()
nums = num.split()
nums = list(map(int, nums))
nums.sort()
n = len(nums)

def find_missing_nums(nums):
    i = 1
    list1 = list()
    for i in range(1,n+1):
        if i not in nums:
            list1.append(i)
    return list1

print(find_missing_nums(nums))
