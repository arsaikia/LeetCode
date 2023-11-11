class Solution:
    def checkPalindrome(self, st, left, right):
        while left > -1 and right < len(st) and st[left] == st[right]:
            left -= 1
            right += 1
        return [left + 1, right]

    def longestPalindrome(self, s: str) -> str:
        longest = float("-inf")
        idx = [-1, -1]
        
        for i in range(len(s)):
            l, r = self.checkPalindrome(s, i, i)
            if r - l > longest:
                longest = r - l
                idx = [l, r]
            
            l, r = self.checkPalindrome(s, i, i + 1)
            if r - l > longest:
                longest = r - l
                idx = [l, r]
        
        return s[idx[0] : idx[1]]     


