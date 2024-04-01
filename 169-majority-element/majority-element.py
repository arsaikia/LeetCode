class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore algorithm
        # Very Very Important

        candidate = nums[0]
        votes = 0

        for num in nums:
            if num == candidate:
                votes += 1
            elif votes > 0:
                votes -=1
            else:
                candidate = num
                votes = 1
        
        return candidate


            
            
        