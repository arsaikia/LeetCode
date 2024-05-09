# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        firstBad = -1

        while l <= r:
            m = (l + (r - l) // 2)
            isBad = isBadVersion(m)

            if isBad:
                firstBad = m
                r = m - 1
            else:
                l = m + 1
        
        return firstBad

        