import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMap = {i : [] for i in range(n)}
        for s, d, price in flights:
            adjMap[s].append([d, price])
        
        cost = [float("inf") for _ in range(n)]

        minHeap = collections.deque([[0, src]])

        for __ in range(k + 1):
            if not minHeap:
                break

            for __ in range(len(minHeap)):
                currPrice, currNode = minHeap.popleft()
                
                for nextNode, nextPrice in adjMap[currNode]:
                    if currPrice + nextPrice < cost[nextNode]:
                        cost[nextNode] = currPrice + nextPrice
                        minHeap.append([currPrice + nextPrice, nextNode])    
        
        return cost[dst] if cost[dst] != float("inf") else -1
            

        