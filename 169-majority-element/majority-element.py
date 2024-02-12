class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        maj = len(nums) // 2

        for key, val in counts.items():
            if val > maj:
                return key
        