class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        r1=defaultdict(int)
        c1=defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    r1[i]+=1
                    c1[j]+=1
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    ans+=(r1[i]-1)*(c1[j]-1)
        return ans
                
        