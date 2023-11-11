import heapq
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adjMap = collections.defaultdict(list)
        for src, dst, cost in edges:
            self.adjMap[src].append( (cost, dst) )
        

    def addEdge(self, edge: List[int]) -> None:
        src, dst, cost = edge
        self.adjMap[src].append( (cost, dst) )
        

    def shortestPath(self, src: int, dst: int) -> int:
        n = len(self.adjMap)
        minHeap = [ [0, src] ]
        visited = set()
        
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)

            if node == dst:
                return cost
            
            for c, nei in self.adjMap[node]:
                heapq.heappush(minHeap, [cost + c, nei])
        
        return -1


        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)