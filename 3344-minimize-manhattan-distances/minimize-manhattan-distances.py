class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        a1 = a2 = b1 = b2 = None
        minSum = minSum2nd = minDiff = minDiff2nd = float('inf')
        maxSum = maxSum2nd = maxDiff = maxDiff2nd = float('-inf')
        ans = float('inf')
        for i, (x, y) in enumerate(points):
            if x + y < minSum:
                a1 = i
                minSum, minSum2nd = x + y, minSum
            elif x + y < minSum2nd:
                minSum2nd = x + y
            if x + y > maxSum:
                a2 = i
                maxSum, maxSum2nd = x + y, maxSum
            elif x + y > maxSum2nd:
                maxSum2nd = x + y
            if x - y < minDiff:
                b1 = i
                minDiff, minDiff2nd = x - y, minDiff
            elif x - y < minDiff2nd:
                minDiff2nd = x - y
            if x - y > maxDiff:
                b2 = i
                maxDiff, maxDiff2nd = x - y, maxDiff
            elif x - y > maxDiff2nd:
                maxDiff2nd = x - y

        for i in {a1, a2, b1, b2}:
            Al = minSum2nd if i == a1 else minSum
            Ar = maxSum2nd if i == a2 else maxSum
            Bl = minDiff2nd if i == b1 else minDiff
            Br = maxDiff2nd if i == b2 else maxDiff
            ans = min(ans, max(Ar - Al, Br - Bl))
        return ans