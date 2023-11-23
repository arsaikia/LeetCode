import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        charCounter = collections.Counter(nums)
        minHeap = [(-val, key) for key, val in charCounter.items()]
        heapq.heapify(minHeap)

        res = []
        while k:
            val, key = heapq.heappop(minHeap)
            res.append(key)
            k -= 1
        
        return res


        