from collections import Counter, defaultdict, deque
import heapq
from typing import List

class KthLargestInStream:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap , self.K = nums ,k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.K :
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)

        if len(self.minHeap) > self.K :
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
class Heap:
    def __init__(self):
        self.min_heap = []

    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) ==0 :
            return 0
        stone = [-s for s in stones]
        heapq.heapify(stone)

        while len(stone) > 1:
            stone1 = heapq.heappop(stone)
            stone2 = heapq.heappop(stone)

            if stone2 > stone1:
                heapq.heappush(stone, stone1 - stone2)

        stone.append(0)

        return abs(stone[0])


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points :
            distance = x**2 + y**2
            minHeap.append([distance,x,y])
        
        heapq.heapify(minHeap)
        res =[]
        while k> 0:
            distance,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res

        

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # easiest way of the solution sort the list and return nums[len(nums)-k]
        #  we can solve this using min heap too .
         k = len(nums)-k
         def quickSelect(l,r):
             pivot , p = nums[r] ,l
             for i in range(l,r):
                 if nums[i] <= pivot :
                     nums[p] ,nums[i] = nums[i] ,nums[p]
                     p+=1
             nums[p],nums[r] = nums[p],nums[r] 

             if p>k : return quickSelect(l,p-1)
             elif p<k: return quickSelect(p+1 ,r)
             else : return nums[p]
         return quickSelect(0,len(nums)-1)


    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time =0 
        q= deque()

        while maxHeap or q :
            time += 1

            if maxHeap :
                cnt = 1+ heapq.heappop(maxHeap)
                if cnt :
                    q.append([cnt ,time+n])
            if q and q[0][1] == time :
                heapq.heappush(maxHeap,q.popleft()[0])
        return time

        

        

class Twitter:
    def __init__(self):
        self.count =0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId :int, tweetId:int):
        self.tweetMap[userId].append([self.count ,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId:int):
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId] :
            if followeeId in self.tweetMap :
                index = len(self.tweetMap[followeeId]) -1
                count ,tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count ,tweetId,followeeId,index-1])

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10 :
            count ,tweetId,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0 :
                count ,tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap ,[count,tweetId,followeeId ,index-1])

        return res

    def follow(self, followerId:int, followeeId : int):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId:int, followeeId:int):
        if followeeId in self.followMap[followerId] :
            self.followMap[followerId].remove(followeeId)

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        pass

    def findMedian(self):
        pass
