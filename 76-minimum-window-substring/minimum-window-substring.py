class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
            
        charsInT, charsInS = collections.Counter(t), collections.defaultdict(int)

        l = 0
        have, need = 0, len(charsInT)
        longest, res = float("inf"), [-1, -1]

        for r in range(len(s)):
            # if have == need and r - l + 1 < longest:
            #     res = [l, r]
            #     longest = r - l + 1
            
            # open window
            if s[r] in charsInT:
                charsInS[s[r]] += 1
                if charsInS[s[r]] == charsInT[s[r]]:
                    have += 1
            
            # close window
            while have == need:
                if r - l + 1 < longest:
                    res = [l , r]
                    longest = r - l + 1
                
                if s[l] in charsInT:
                    charsInS[s[l]] -= 1

                    if charsInS[s[l]] + 1 == charsInT[s[l]]:
                        have -= 1
                
                l += 1
        
        l, r = res
        return s[l : r + 1] if longest != float("inf") else ""



        