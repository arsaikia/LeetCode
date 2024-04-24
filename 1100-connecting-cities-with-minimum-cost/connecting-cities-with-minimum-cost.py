import heapq
class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.ranks = {}
        for i in range(1, n + 1):
            self.parents[i] = i
            self.ranks[i] = 1
    
    # finds topmost parent of given node
    def find(self, n):
        parent = self.parents[n]
        grandParent = self.parents[parent]

        while parent != grandParent:
            self.parents[parent] = self.parents[grandParent]
            parent = self.parents[parent]
            grandParent = self.parents[parent]

        return parent
    
    # check if nodes can be combined -> No cycle -> return False, else return True
    def union(self, m, n):
        p1, p2 = self.find(m), self.find(n)
        
        if p1 == p2:
            return True
        
        if self.ranks[p1] > self.ranks[p2]:
            self.ranks[p1] += self.ranks[p2]
            self.parents[p2] = p1
        else:
            self.ranks[p2] += self.ranks[p1]
            self.parents[p1] = p2
        
        return False

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        minHeap = []
        
        for a, b, w in connections:
            heapq.heappush(minHeap, (w, a, b) )
            heapq.heappush(minHeap, (w, b, a) )
        
        mst = []
        cost = 0

        while minHeap and len(mst) < n - 1:
            weight, src, dst = heapq.heappop(minHeap)
            if uf.union(src, dst):
                continue
            
            mst.append( [src, dst] )
            cost += weight
        
        return cost if len(mst) == n - 1 else -1



        

        