class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # We are guranteed to have a duplicate
        # using Floyd's Torroise and Hare algorithm we can find the cycle
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
