class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        
        count = collections.defaultdict(list)

        for key, val in counts.items():
            count[val].append(key)
        
        sortedCount = []
        for num, vals in count.items():
            sortedCount.append((num, vals))

        sortedCount.sort(reverse=True)

        res = []
        for i in range(k):
            if k == 0:
                    break
            currVals = sortedCount[i][1]
            for val in currVals:
                if k == 0:
                    break
                res.append(val)
                k -= 1

        return res