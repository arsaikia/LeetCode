class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        minSpeed = piles[-1]

        while l <= r:
            m = l + (r - l) // 2
            eatingSpeed = m
            canFinish = self.canfinishAllPiles(piles, h, eatingSpeed)

            if canFinish:
                minSpeed = eatingSpeed
                r = m - 1
            else:
                l = m + 1
        
        return minSpeed
    
    def canfinishAllPiles(self, piles, h, eatingSpeed):
        endIdx = len(piles) - 1
        timeNeeded = 0
        idx = 0

        for pile in piles:
            h -= math.ceil(pile / eatingSpeed)
            if h < 0:
                return False
        
        if h >= 0:
            return True
        return False
        
        



            
            

            




        