class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(key = lambda x : -x)

        res = 0
        i = 0
        j = 0

        # if the kth element is < k, take that first or we will get to 0
        # while happiness[k - 1] < k:
        #     val = happiness[k - 1]
        #     res += val
        #     k -= 1
        #     j += 1

        while i < k:
            val = happiness[i] + (-1 * (i + j))
            res += val if val > 0 else 0

            if val <= 0:
                break

            i += 1
        
        return res
        