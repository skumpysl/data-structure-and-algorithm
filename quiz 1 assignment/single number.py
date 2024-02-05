def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
nums = [4,4,2,1,2]
print(singleNumber(nums))