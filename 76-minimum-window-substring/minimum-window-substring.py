class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        charsInS, charsInT = collections.defaultdict(int), collections.defaultdict(int)
        for ch in t:
            charsInT[ch] += 1

        have, need = 0, len(charsInT)
        res, size = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            if have == need and r - l + 1 < size:
                res = [l, r]
            
            # open window
            if s[r] in charsInT:
                charsInS[s[r]] += 1
                if charsInS[s[r]] == charsInT[s[r]]:
                    have += 1
            
            # close window
            while have == need:
                if r - l + 1 < size:
                    size = r - l + 1
                    res = [l, r]
                
                # close from l
                if s[l] in charsInT:
                    charsInS[s[l]] -= 1
                    if charsInS[s[l]] + 1 == charsInT[s[l]]:
                        have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if size != float("inf") else ""

        

        