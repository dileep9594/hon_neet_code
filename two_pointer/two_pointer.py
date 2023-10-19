

from ast import List


def alphanumeric(s):
    return ( (ord("A") <= ord(s) <= ord("Z")) or 
    (ord("a") <= ord(s) <= ord("z")) or
    (ord("0") <= ord(s) <= ord("9")) ) 
        
def validPalidrome(s:str):
    l,r = 0, len(s)-1

    while l<r :
        while l<r and not alphanumeric(s[l]) :
            l=l+1
        while r>l and alphanumeric(s[r]) :
            r-=1

        if s[l].lower() != s[r].lower():
            return False



def twoSumiiInputArrayIsSorted(numbers,target):
    l,r = 0,len(numbers)-1
    while l<r :
        if numbers[l]+numbers[r] == target :
            return [l+1,r+1]
        elif numbers[l] + numbers[r] > target :
            r-=1
        else : l+=1
    return []

def threeSum(nums:List[int]) -> List[List[int]]:
    nums.sort()
    res =[]
    for i,a in enumerate(nums):
        if i>0 and a == nums[i-1] :
            continue
            
        l,r=i+1 ,len(nums)-1
        while l<r :
            threeSum = a+nums[l]+nums[r]
            if threeSum > 0 :
                r-=1
            elif threeSum < 0 :
                l+=1
            else :
                res.append([a,nums[l],nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return res

def containerWithMostWater(height :List[int]) -> int:
    l,r  = 0,len(height)-1 
    mostWater =0
    while l<r :
        container = (r-l) * min(height[l],height[r])
        mostWater = max(container,mostWater)
        if height[l]<height[r] :
            l+=1
        else :
            r-=1
    return mostWater

def trappingRainWater(height :List[int]) -> int:
    l,r = 0,len(height)-1
    leftMax ,rightMax  = height[l] ,height[r]
    res =0
    while l<r :
        if height[l]<height[r] :
            l+= 1
            leftMax = max(height[l],leftMax)
            res+= leftMax-height[l]
        else :
            r-=1
            rightMax = max(rightMax,height[r])       
            res += rightMax-height[r]

    return res

