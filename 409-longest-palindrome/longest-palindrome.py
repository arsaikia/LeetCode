class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)

        hasOdd = False
        res = 0

        for num in counts.values():
            if num % 2 == 0:
                res += num
            else:
                res += (num // 2) * 2
                hasOdd = True
        
        return res + 1 if hasOdd else res

        