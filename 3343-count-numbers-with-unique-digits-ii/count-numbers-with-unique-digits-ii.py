class Solution:
    def numberCount(self, a: int, b: int) -> int:

        def hasUniqueDigits(n):
            numStr = str(n)
            seen = set()
            for c in numStr:
                if c in seen:
                    return False
                seen.add(c)
            
            return True
        
        count = 0
        for num in range(a, b + 1):
            if not hasUniqueDigits(num):
                count += 1
            
        
        return b - a - count + 1
        