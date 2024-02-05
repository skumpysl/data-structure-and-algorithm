def summation(nums):
    return sum(nums)

def maximum(nums):
    return max(nums)

def main():
    n = int(input("Enter the number of elements in the array: "))
    nums = []
    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        nums.append(num)
    
    print(f"The sum of the elements is: {summation(nums)}")
    print(f"The maximum element is: {maximum(nums)}")
main()