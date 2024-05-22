class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # monotically decreasing q
        q = collections.deque([])

        l = 0
        res = []

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()

            while r - l + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        
        return res

        