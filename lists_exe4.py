nums = [1, 2, 2, 3]
num_to_remove = 2
if num_to_remove in nums:
    if nums.count(num_to_remove)>1:
        nums.remove(num_to_remove)
        print(nums)
    else:
        print("The number you want to remove exsist only one time")    
else:
    print("The number you want to remove doesn't exsist in the list")