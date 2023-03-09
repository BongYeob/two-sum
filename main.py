def twoSum( nums, target):
    result = []

    for i in range(0, len(nums)):
        if (nums[i] >= target):
            continue

        for j in range(i+1, len(nums)):
            if(nums[i]+nums[j]==target):
                result = [i,j]
                break
        
        if(len(result)==2):
            break

    return result