class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.strip()
        
        j = len(st) - 1
        while j >= 0 and st[j] != " ":
            j -= 1
        
        return len(st) - j - 1
            
        
        
            

        