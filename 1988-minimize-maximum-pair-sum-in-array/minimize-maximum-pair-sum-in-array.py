class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        minHeap, maxHeap = nums, [-num for num in nums]
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)

        maxPairSum = 0

        for idx in range(len(nums)//2):
            minValue, maxValue = heapq.heappop(minHeap), -1 * heapq.heappop(maxHeap)
            currPairSum = minValue + maxValue
            maxPairSum = max(maxPairSum, currPairSum)
        
        return maxPairSum


        