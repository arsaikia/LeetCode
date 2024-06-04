class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, large = nums1, nums2
        if len(nums1) > len(nums2):
            small, large = large, small
        
        smallSize, largeSize = len(small), len(large)
        halfSize = (smallSize + largeSize) // 2   # This is what we want our partitions size to be

        l, r = 0, len(small) - 1
        
        while True:
            smallPivot = l + (r - l) // 2
            largePivot = (halfSize - 2) - smallPivot

            smallLeft = small[smallPivot] if smallPivot >= 0 else float("-inf")
            smallRight = small[smallPivot + 1] if (smallPivot + 1) < smallSize else float("inf")
            largeLeft = large[largePivot] if largePivot >= 0 else float("-inf")
            largeRight = large[largePivot + 1] if (largePivot + 1) < largeSize else float("inf")

            # partition is correct
            if smallLeft <= largeRight and largeLeft <= smallRight:
                # ODD
                if (smallSize + largeSize) % 2:
                    return min(smallRight, largeRight)
                else:
                    return (max(smallLeft, largeLeft) + min(smallRight, largeRight)) / 2
            elif smallLeft > largeRight:
                r = smallPivot - 1
            else:
                l = smallPivot + 1
        