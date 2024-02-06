from typing import List


class Backtracking:
    def subsets(self, nums):
        result = []
        subsets = []
        def backtrack(i) :
            if i>= len(nums):
                result.append(subsets.copy())
                return
            subsets.append(nums[i])
            backtrack(i+1)
            subsets.pop()
            backtrack(i+1)
        backtrack(0)
        return result    

    def combinationSum(self, candidates, target):
        result = []
        def backtrack(i,cur,total):
            if total == target :
                result.append(cur.copy())
                return
            if i >= len(candidates) or total > target :
                return
            
            cur.append(candidates[i])
            backtrack(i,cur,total+candidates[i])
            cur.pop()
            backtrack(i+1,cur,total)
        backtrack(0,[],0)
        return result
            


    def permutations(self, nums):
        result = []
        if len(nums) == 1 :
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permutations(nums)
            for perm in perms :
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i,subset):
            if i == len(nums):
                res.append(subset[::])
                return  
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
            while i+1 <len(nums) and nums[i] == nums[i+1] :
                i+=1
            backtrack(i+1,subset)

        backtrack(0,[])
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(cur,pos,target):
            if target == 0 :
                res.append(cur.copy())
            if target <= 0:
                return
            prv = -1
            for i in range(pos,len(candidates)) :
                if candidates[i] == prv :
                    continue
                cur.append(candidates[i])
                backtrack(cur,i+1,target-candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack([],0,target)
        return res

    def exist(self, board: List[List[str]], word: str) -> bool: #wordSearch problem
        rows ,cols = len(board) , len(board[0])
        path = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if r< 0 or c< 0 or r >= rows or c >= cols or word[i] != board[r][c] or ((r,c) in path ) :
                return False
            path.add((r,c)) 
            res = (dfs(r+1,c,i+1) or
            dfs(r,c+1,i+1) or
            dfs(r,c-1,i+1) or
            dfs(r-1,c,i+1) )
            path.remove((r,c))
            return res 

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0) : return True
        return False

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return 
            for j in range(i,len(s)):
                if self.isPalidrome(s,i,j) :
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

    def isPalidrome(self,s,l,r):
        while l <= r :
            if s[l] != s[r] :
                return False
            l,r = l+1,r-1
        return True

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2":"abc" ,
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtrack(i,curStr):
            if len(curStr) == len(digits) :
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i+1,curStr+c)
        if digits:
            backtrack(0,"")
        return res

    def solveNQueens(self, n):
        pass

if __name__ == '__main__':
    
    Bt = Backtracking()
    a = [2,3,6]
    print(Bt.permutations(a))

