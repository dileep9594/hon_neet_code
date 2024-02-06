class Dp1D:

    def __init__(self) :
        self.name = 'Dp1D'
    def climbStairs(self, n:int) -> int:
        if n ==0 or n==1 :
            return 1
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def minCostClimbingStairs(self, cost) -> int:
        for i in range(len(cost)-3,-1,-1) :
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1]) 
        

    def houseRobber(self, nums ) ->int:
        n= len(nums)
        if n<=2 :
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n) :
            dp[i] = max(dp[i-2]+nums[i],dp[i-1]) #mistake  was doing not leaving adjacent house
        return dp[-1]
    
    def houseRobberSpaceOptimized(self, nums) ->int:
        rob1,rob2 = 0 ,0
        for n in nums :
            temp = max(n+rob1,rob2) 
            rob1 = rob2
            rob2 = temp
        return rob2
    


    def houseRobberII(self, nums):
        # same as houseRobber with handling edge cases
        pass


    def longestPalindromicSubstring(self, s):
        res = "" 
        resLen =0
        for i in range(len(s)):
            #odd length palidrome
            l,r =i ,i
            while l>=0 and r< len(s) and s[l] == s[r] :
                if (r-l+1) > resLen :
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            # even length strings are
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) >resLen :
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return res

    def countPali(self,s,l,r) :
            res =0 
            while l>=0 and r < len(s) and s[l] == s[r] :
                res+=1
                l-=1
                r+=1
            return res

    def countSubstrings(self, s: str) -> int:
        res =0
        for i in range(len(s)):
            res += self.countPali(s,i,i)
            res += self.countPali(s,i,i+1)
        return res

    def decodeWays(self, s):
        pass

    def coinChange(self, coins, amount:int)-> int:
        dp =[amount+1]*(amount+1)
        dp[0] =0
        for a in range(amount+1):
            for c in coins :
                if a>=c :
                    dp[a] = min(dp[a],1+dp[a-c])
                    
        return dp[amount] if dp[amount] != amount+1 else -1 
    
    def printcoinChange(self, coins, amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        used_coins = [[] for _ in range(amount + 1)]  # List to store used coins for each amount

        for a in range(amount + 1):
            for c in coins:
                if a >= c and 1 + dp[a - c] < dp[a]:
                    dp[a] = 1 + dp[a - c]
                    used_coins[a] = used_coins[a - c] + [c]

        if dp[amount] == amount + 1:
            return -1
        else:
            print("Coins used:", used_coins[amount])  # Print the coins used
            return dp[amount]
        
    def maxProductSubarray(self, nums):
        pass

    def wordBreak(self, s, wordDict):
        pass

    def lengthOfLIS(self, nums):
        pass

    def canPartition(self, nums):
        pass

class Dp2D:
    def uniquePaths(self, m, n):
        pass

    def longestCommonSubsequence(self, text1, text2):
        pass

    def maxProfitWithCooldown(self, prices):
        pass

    def changeCoins(self, amount, coins):
        pass

    def findTargetSumWays(self, nums, S):
        pass

    def isInterleave(self, s1, s2, s3):
        pass

    def longestIncreasingPath(self, matrix):
        pass

    def numDistinct(self, s, t):
        pass

    def minDistance(self, word1, word2):
        pass

    def maxCoins(self, nums):
        pass

    def isMatch(self, s, p):
        pass

if __name__=='__main__':
    edp = Dp1D()
    coins = [1,2,5]
    amount = 11
    minCoin = edp.printcoinChange(coins,amount)
    used_coins = [[] for _ in range(amount + 1)]
    print(used_coins)
    print(edp.name)
