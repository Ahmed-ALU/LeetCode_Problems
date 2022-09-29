def threeSum(nums)->list:

    
    length = len(nums)
    result = []


    if length < 3:
        return []

    for i in range(0,length):
        # x+=1
        for j in range(0,length):
            # y+=1
            for k in range(0,length):
                # z+=1
                if i!=j and j!=k and i!=k:
                    sum = nums[i] + nums[j] + nums[k]
                    lis = sorted([nums[i] ,nums[j], nums[k]])
                    if sum == 0 and lis not in result:
                        result.append(lis)
        
    return result

print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,0,0,0]))