def sortedSquares(nums):
    L = 0
    R = L+1
    n = len(nums)
    
    while L < n-1:
        if R == n-1 and L == n-2:
            nums[L], nums[R] = nums[L]**2, nums[R]**2
            return nums
    
        if abs(nums[L])<abs(nums[R]) or abs(nums[L])== abs(nums[R]):
            R+=1
            
        else:
            nums[L], nums[R] = nums[R]**2, nums[L]
            L+=1
            R = L+1
        

    return nums

print(sortedSquares([-7,-3,2,3,11]))

#[1, , 0, 3, 4]
# *  *

