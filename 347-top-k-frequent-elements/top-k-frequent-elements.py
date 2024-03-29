class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(list)

        counter = collections.Counter(nums)
        for num, cnt in counter.items():
            count[cnt].append(num)
        
        res = []

        for vals in reversed(sorted(count.keys())):
            for val in count[vals]:
                if k > 0:
                    res.append(val)
                    k -= 1
        return res