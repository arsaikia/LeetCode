class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                return None

            return generate(curr + "1") or generate(curr + "0")

        n = len(nums)
        nums = set(nums)
        return generate("")