import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMap = {i : [] for i in range(n)}
        for s, d, price in flights:
            adjMap[s].append([d, price])
        
        cost = [float("inf") for _ in range(n)]

        q = collections.deque([[0, src]])

        for __ in range(k + 1):
            if not q:
                break

            for __ in range(len(q)):
                currPrice, currNode = q.popleft()
                
                for nextNode, nextPrice in adjMap[currNode]:
                    if currPrice + nextPrice < cost[nextNode]:
                        cost[nextNode] = currPrice + nextPrice
                        q.append([currPrice + nextPrice, nextNode])    
        
        return cost[dst] if cost[dst] != float("inf") else -1
            

        