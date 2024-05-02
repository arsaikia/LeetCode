import heapq
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        minHeap = nums[:]
        maxHeap = [-1 * num for num in nums]
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)
        while minHeap and maxHeap:
            minVal, maxVal = minHeap[0], -1 * maxHeap[0]


            if -1 * minVal == maxVal:
                return maxVal
            elif -1 * minVal > maxVal:
                heapq.heappop(minHeap)
            else:
                heapq.heappop(maxHeap)
            

        return -1

        