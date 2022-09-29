def threeSum(nums)->list:
    # [-4,-1,-1,0,1,2] sorted
    #         > < <
    #Initiate Variables

    initial = 0
    loP = 1
    length = len(nums)
    hiP = length-1
    result = []
    
    #sort the array
    nums = sorted(nums)

    #algorithm
    # [3,0,-2,-1,1,2]
    
    if length <3:
        return result
    
    while initial <= length -3:
        sum = nums[initial] + nums[loP] + nums[hiP]
        lis = sorted([nums[initial] , nums[loP] , nums[hiP]])

        if sum == 0 and lis not in result and (initial != loP != hiP):
            result.append(lis)
            if abs(hiP - loP) == 1:
                initial +=1
                loP = initial +1
                hiP = length-1
                continue
            elif length - hiP > initial - loP :
                loP +=1
            elif length - hiP < initial - loP:
                hiP -=1
        elif sum < 0 and loP < hiP-1:    
            loP += 1
            continue
        
        elif sum > 0 and loP < hiP-1:
            hiP -= 1
            continue

        else:
            if sum == 0 and loP < hiP-1:
                if length - hiP > initial - loP :
                    loP +=1
                elif length - hiP < initial - loP :
                    hiP -=1
            else:
                initial +=1
                loP = initial +1
                hiP = length-1
    
    return result

        
# print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
# print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,0,0,0]))