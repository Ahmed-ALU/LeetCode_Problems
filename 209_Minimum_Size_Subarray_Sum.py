from turtle import up


def run(nums, target):
    up = 0
    lo = 0 
    temp01 = []
    temp02 = []
    arrLen = len(nums)
    Sum = int()

    while up < arrLen:

        if up == lo:

            if nums[up] >= target:
                temp01 = [nums[up]]
                up+=1
                if lo < arrLen -1:
                    lo+=1
                else: 
                    up += 1
            elif nums[up] < target:
                if lo < arrLen -1:
                    lo+=1
                else: 
                    up += 1

        elif up != lo:

            temp02 = []
            Sum = 0
            for i in range(up, lo+1):
                Sum += nums[i]
                temp02.append(nums[i])
            if Sum >= target and len(temp01) > lo-up+1:
                temp01 = temp02
                up+=1
                if lo < arrLen -1:
                    lo+=1
                else: 
                    up += 1
            elif Sum >= target and len(temp01) < lo-up+1:
                up+=1
                if lo < arrLen -1:
                    lo+=1
            elif Sum < target:
                if lo < arrLen -1:
                    lo+=1
                else: 
                    up += 1
    if temp01 == []:
        return temp02
    elif sum(temp01) < target and sum(temp02) < target:
        return 0
    else:
        return temp01

print(run([2,3,1,2,4,3], 7))
print(run([1,4,4], 4))

                

        
            
