def removeDuplicates(nums) -> int:
    L = 0
    R = L+1
    n = len(nums)

    if len(nums) < 2:
        return n
    
    while R < n:
        if nums[L] == nums[R]:
            R+=1
        elif nums[L] != nums[R]:
            if R-L == 1:
                nums[L+1], nums[R] = nums[R], nums[L+1]
                L+=1
                R+=1
            else:
                nums[L+2], nums[R] = nums[R], nums[L+2]
                L+=1
                R+=1
    
    return L+2, nums
            