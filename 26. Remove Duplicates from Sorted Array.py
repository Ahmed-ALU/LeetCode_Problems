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
                L+=1
                R+=1
            else:
                nums[L+1], nums[R] = nums[R], nums[L+1]
                L+=1
                R+=1
    
    return L+1, nums

print(removeDuplicates([1, 2, 3, 1, 1, 1, 3, 2]))



#[0,0,0,1,1,2,2,3,4]
# *     *
        
# [0,1,2,3,4,2,1,0,4]
#          *       *
                