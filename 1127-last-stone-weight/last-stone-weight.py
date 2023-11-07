class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            firstStone = -1 * heapq.heappop(maxHeap)
            secondStone = -1 * heapq.heappop(maxHeap)
            if firstStone == secondStone:
                continue
            heapq.heappush(maxHeap, -1 * abs(firstStone - secondStone))
        
        return -1 * maxHeap[0] if len(maxHeap) else 0
        