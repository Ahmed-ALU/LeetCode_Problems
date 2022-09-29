class Solution:
    def maxArea(self, height) -> int:
        
        pl = 0 
        pr = len(height)-1
        a = 0 
        
        area = lambda w,h : w*h
        width = len(height)-1

        while pl != pr:
            
            at = area(width, min([height[pl], height[pr]]))
            
            if at > a :
                a = at
            if height[pl] > height[pr]:
                pr-=1
                width -=1
            else:
                pl+=1
                width-=1
                    
        return a
                
        
        