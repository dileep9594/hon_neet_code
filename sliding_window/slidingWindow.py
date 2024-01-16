from typing import List
import collections


class SlidingWindow :
    def bestTimetoBuyAndSellStock(self,prices:List[int]) -> int:
        l =0
        profit =0
        for r in range(1,len(prices)):
            if prices[l]<prices[r]:
                profit = max(profit,prices[r]-prices[l])
            else :
                l=r
        return profit
    def longestSubstringWithoutRepeatingCharacters(self,s:str) -> int:
        subString  = set()
        l =0
        res = 0
        for r in range(len(s)):
            while s[r] in subString :
                subString.remove(s[l])
                l += 1
            subString.add(s[r])

            res = max(res,r-l+1)
        
        return res

        
        

    def longestrepeatingCharacterReplacement(self,  s:str,k:int):
        count = {}
        res =0
        l =0
        for r in range(len(s)) :
            count[s[r]] = 1+count.get(s[r],0)
            while (r-l+1) - max(count.values()) >k :
                count[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res


    def permutationInString(self,s1,s2):
        if len(s1) > len(s2) : return False
        s1Count ,s2Count =[0]*26 ,[0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i] - ord('a'))] +=1
            s2Count[ord(s2[i] - ord('a'))] +=1

        matches =0 
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        l=0 
        for r in range(len(s1),len(s2)):
            if matches == 26 : return True

            index = ord(s2[r]-ord('a'))
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]+1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]-ord('a'))
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]-1 == s2Count[index]:
                matches -= 1
            l+=1
        return matches == 26

    def minimumWindowSubstring(self,t:str ,s:str):
        if t == " " : return ""

        countT ,window = {},{}

        for c in t :
            countT[c] = 1+ countT.get(c,0)
        
        have ,need  = 0 , len(countT)
        res ,reslen = [-1,-1] ,float("infinity")
        l=0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+ window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need :
                if (r-l+1) <reslen :
                    res = [l,r]
                    reslen =  (r-l+1)
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        l ,r =  res
        return s[l:r+1] if reslen != float("infinity") else ""


    def slidingWindowMaximum(self,nums,k):
        result =[]
        q = collections.deque()
        l =r =0
        while r < len(nums) :
            while q and nums[q[-1]] < nums[r] :
                q.pop()
            q.append(r)

            if l > q[0] :
                q.popleft()
            
            if (r+1) >= k :
                result.append(nums[q[0]])
                l+=1
            r += 1
        return result

        



if __name__ == '__main__':
    sd = SlidingWindow()
    print("SlidingWindow")