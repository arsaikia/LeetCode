
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i : [] for i in range(n)}
        for src, dst in edges:
            adjMap[src].append(dst)
            adjMap[dst].append(src)

        visited = set()

        def dfs(node, prev):
            nonlocal visited

            if node in visited:
                return False
            
            visited.add(node)

            for nxt in adjMap[node]:
                if nxt == prev:
                    continue
                if not dfs(nxt, node):
                    return False
            return True
            
        return dfs(0, -1) and n == len(visited)