def find_average(nums):
    total = 0
    for num in nums:
        total+=num
    return total/len(nums) if nums != [] else 0
