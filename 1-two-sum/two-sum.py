class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = collections.defaultdict(int)

        for idx, num in enumerate(nums):
            required = target - num
            if required in seen:
                return [seen[required], idx]
            
            seen[num] = idx
        
        return [-1, -1]
        