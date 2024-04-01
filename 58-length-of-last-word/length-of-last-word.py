class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastValidIdx = -1
        firstValidIdx = -1

        idx = len(s) - 1

        while idx >= 0:
            if lastValidIdx != -1 and firstValidIdx != -1:
                break
            
            char = s[idx]
            
            # set firstValidIdx
            if lastValidIdx != -1 and char == " ":
                firstValidIdx = idx

            # set lastValidIdx
            if char != " " and lastValidIdx == -1:
                lastValidIdx = idx


            idx -= 1

        return (lastValidIdx - firstValidIdx)
            
        
        
            

        