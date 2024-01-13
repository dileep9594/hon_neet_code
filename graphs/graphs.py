from collections import deque
import collections
class Node(object):
    pass

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

    def printGraph(self, graph):
        print(graph)

    def dfs(self, graph,node):
        print(node)
        self.visited.add(node)
        for child in graph[node]:
            if child not in self.visited:
                self.dfs(graph, child)
        
    def bfs(self,grid ,r,c):
            q = collections.deque() 
            self.visited.add((r,c))
            q.append((r,c))
            while q :
                row ,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions :
                    r,c = row +dr , col +dc
                    if (r in range(len(grid))) and (c in range(len(grid[0]))) and (self.graph[r][c] == "1") and ((r,c) not in self.visited) :
                        q.append((r,c))
                        self.visited.add((r,c))

    def numIslands(self, grid):
        numOfIsland =0 
        row,col  = len(grid) , len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in self.visited :
                    numOfIsland+=1
                    self.bfs(grid,r,c) 
                    
        return numOfIsland
    
    def noOfConnectedComponents(self,graph):
        noOfConnectedComponents =0 
        for node in graph:
            if node not in self.visited :
                self.dfs(graph,node)
                noOfConnectedComponents+=1
        return noOfConnectedComponents



    def cloneGraph(self, node):
        oldToNew = {}
        def dfs_helper(node):
            if node in oldToNew :
                return oldToNew[node] 
            copy = Node(node.val)
            oldToNew[node] = copy
            for node in node.neighbors :
                copy.neighbors.append(dfs_helper(node))
            return copy
        return dfs_helper(node) if node else None


    def maxAreaOfIsland(self, grid):
        row,col = len(grid) , len(grid[0])
        answer = 0
        visited = set()

        def dfs(r,c):
            if r<0 or r>= row or c< 0 or c>=col or grid[r][c] ==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))      

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 :
                    answer = max(answer,dfs(r,c))
        return answer

    def pacificAtlantic(self, matrix):
        pass

    def surroundedRegions(self, board):
        pass

    def orangesRotting(self, grid):
        pass

    def wallsAndGates(self, rooms):
        pass

    def canFinish(self, numCourses, prerequisites):
        pass

    def findOrder(self, numCourses, prerequisites):
        pass

    def findRedundantConnection(self, edges):
        pass

    def countComponents(self, n, edges):
        pass

    def validTree(self, n, edges):
        pass

    def ladderLength(self, beginWord, endWord, wordList):
        pass


if __name__ == '__main__':
    #  G = (V,E)
    # vertices = 5
    # edges = [[1,2],[1,3],[2,3],[3,4],[4,1]]
    # gr = {i : [] for i in range(1,vertices) }
    # for (u,v) in edges :
    #     gr[u].append(v)
    #     gr[v].append(u)
#     gr = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    graph = Graph(grid)
    # graph.printGraph(gr)  # print the graph
    # print(graph.dfs(gr,1)) # Depth frist search of the graph
    # print(graph.numIslands(gr))
    print(graph.maxAreaOfIsland(grid))

