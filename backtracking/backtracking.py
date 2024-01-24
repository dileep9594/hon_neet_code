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
        pass

    def subsetsWithDuplicates(self, nums):
        pass

    def combinationSumWithDuplicates(self, candidates, target):
        pass

    def wordSearch(self, board, word):
        pass

    def palindromePartitioning(self, s):
        pass

    def letterCombinations(self, digits):
        pass

    def solveNQueens(self, n):
        pass

if __name__ == '__main__':
    
    Bt = Backtracking()
    a = [2,3,6,7]
    print(Bt.combinationSum(a,7))

