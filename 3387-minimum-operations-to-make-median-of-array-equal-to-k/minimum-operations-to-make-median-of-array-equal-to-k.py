class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        arrSize = len(nums)
        
        left = nums[: arrSize // 2]
        right = nums[arrSize // 2 : ]
        
        result = 0
        
        def findMinOddOps():
            res = 0
            i = 1

            currNum = right[0]
            res += abs(k - currNum)


            while i < len(right):
                # go right
                if right[i] < k:
                    res += k - right[i]
                else:
                    break
                i += 1


            j = len(left) - 1
            while j >= 0:
                if left[j] > k:
                    res += left[j] - k
                else:
                    break
                j -= 1

            return res

        
        return findMinOddOps()
        
        
        
