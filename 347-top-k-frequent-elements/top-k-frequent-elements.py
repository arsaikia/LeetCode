class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        numCount = collections.Counter(nums)

        for num, count in numCount.items():
            buckets[count].append(num)
        
        res = []

        for bucket in reversed(buckets):

            if k == 0:
                break
            
            for num in bucket:
                res.append(num)
                k -= 1
        
        return res
            


        