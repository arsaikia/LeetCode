class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        adjMap = collections.defaultdict(list)
        for i in range(n - 1):
            adjMap[i] = []
        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return False
    
            if destination in adjMap[node]:
                return True
            
            visited.add(node)
            
            for nextNode in adjMap[node]:
                if dfs(nextNode):
                    return True
            
            return False
        
        return dfs(source)


            
        