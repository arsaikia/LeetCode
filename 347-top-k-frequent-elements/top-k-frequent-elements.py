class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # bucket at idx x contains elements with frequency x
        buckets = [[] for __  in range(len(nums) + 1)]
        charCounter = collections.Counter(nums)

        for idx, val in charCounter.items():
            buckets[val].append(idx)
        
        res = []
        for idx in reversed(range(len(buckets))):
            if not k:
                break
            bucket = buckets[idx]
            
            for num in bucket:
                res.append(num)
                k -= 1

        return res



        