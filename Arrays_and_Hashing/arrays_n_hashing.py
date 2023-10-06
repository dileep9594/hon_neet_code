def contains_duplicate(nums):
    seen = set()
    for num in nums :
        if num in seen :
            return True
        seen.add(num)
    return False
        

def validAnagram(s:str,t:str):
     numeric = [0]*26
     for x in s :
        numeric[ord(x)-ord("a")] +=1
     for x in t :
        numeric[ord(x)-ord("a")] -=1
     for x in numeric :
        if x != 0 :
            return False
     return True


def twoSum(nums,target):
    complement = {}
    for i in range(len(nums)):
        comp = target-nums[i]
        if comp in complement:
            return [complement[comp],i]
        complement[nums[i]] = i
    return []

def groupAnagrams(strs):
    res = defaultdict(list)
    for string in strs :
        count = [0]*26 
        for s in string:
            count[ord(s)-ord('a')]+=1 
        
        res[tuple(count)].append(string)
    
    return res.values()

def topKFrequentElement(nums,k):
    count = {}
    freq = [[]for n in range(len(nums)+1)]
    for num in nums :
        count[num] = count.get(num ,0) +1

    for n,c in count.items():
        freq[c].append(n)

    res = []
    for n in range(len(freq)-1 , 0 ,-1):
        for i in freq[n] :
            res.append(i)
            if len(res) == k :
                return res
    return res

def productOfArrayExceptSel(nums):
    res = [1]*(len(nums))
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix 
        prefix *= nums[i]
    postfix =1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]  

    return res

def validSudoku(board):
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if (board[r][c] == "."):
                continue

            if(board[r][c] in rows[r] or board[r][c] in cols[c]
               or board[r][c] in squares[(r//3,c//3)]):
                return False
            
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])
        

    return True

def encodeAndDecodeString(): # for premium accounrs only
    pass

def LongestConsecutiveSequence(nums):
    numSet  = set(nums)
    longest =0 
    for n in nums :
        if n-1 not in numSet : # check if it is the start of sequence
            length = 0 
            while (n+length) in numSet :
                length+= 1
            longest = max(longest,length)
    return longest



if __name__ == "__main__": 
    print(LongestConsecutiveSequence([100,4,200,1,3,2])))