class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        i = len(s) - 1

        # move right pointer to left as long as we have empty string
        # stops when we find a valid character
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # Now move i to left as long as char is not empty string
        while i >= 0 and s[i] != " ":
            i -= 1
            length += 1
        
        return length
        

        