def rotate(nums, k):
    # Ensure k is within the range of the array length
    k = k % len(nums)
    
    # Reverse the entire array, then reverse the first k elements and the rest separately
    nums[:] = nums[-k:] + nums[:-k]

    nums = [1,2,3,4,5,6,7]
nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
print(nums)  