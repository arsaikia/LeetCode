class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(key = lambda x : -x)

        res = 0
        i = 0

        while i < k:
            val = happiness[i] - i
            if val <= 0:
                break

            res += val if val > 0 else 0
            i += 1
        
        return res
        