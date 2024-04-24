import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjMap = {i : [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjMap[i].append((dist, j))
                adjMap[j].append((dist, i))
        
        count, visited, minHeap = 0, set(), [(0, 0)]
        while len(visited) < N:
            currDist, currNode = heapq.heappop(minHeap)
            if currNode in visited:
                continue
            
            visited.add(currNode)
            count += currDist

            for nextDist, nextNode in adjMap[currNode]:
                if nextNode not in visited:
                    heapq.heappush(minHeap, (nextDist, nextNode))
        
        return count

