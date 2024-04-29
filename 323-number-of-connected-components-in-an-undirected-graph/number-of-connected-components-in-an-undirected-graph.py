class DSU:
    def __init__(self, n):
        self.parents = {}
        self.ranks = {}
        self.components = 0

        for i in range(n):
            self.parents[i] = i
            self.ranks[i] = 1
        
        print(self.parents, self.ranks)
        
    def find(self, node):
        parent = self.parents[node]
        grandParent = self.parents[parent]

        while parent != grandParent:
            self.parents[parent] = self.parents[grandParent]
            parent = self.parents[parent]
            grandParent = self.parents[parent]
        return parent
    
    def union(self, p, q):
        p1, p2 = self.find(p), self.find(q)

        if p1 == p2:
            return False # can't join, cycle
        
        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
            self.ranks[p2] += 1
        else:
            self.parents[p1] = p2
            self.ranks[p1] += 1
        self.components += 1
        return True        

        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for a, b in edges:
            dsu.union(a, b)
        
        return n - dsu.components

        