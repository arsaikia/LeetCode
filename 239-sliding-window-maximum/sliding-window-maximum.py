class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # index
        l = 0
        res = []

        for r in range(len(nums)):

            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # remove from left of window
            if l > q[0]:
                q.popleft()

            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1
            
        
        return res

        