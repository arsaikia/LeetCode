import heapq
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        maxHeap = [-val for val in happiness]
        heapq.heapify(maxHeap)
        res, i = 0, 0

        while i < k:
            val = (-1 * heapq.heappop(maxHeap)) - i
            if val <= 0:
                break

            res += val if val > 0 else 0
            i += 1
        
        return res
        