class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        q = collections.deque(nums)

        # base case
        if len(nums) == 1:
            return [nums.copy()]  # q[:] is a deep copy

        for i in range(len(q)):
            n = q.popleft()
            perms = self.permute(q)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            q.append(n)
        return res
