class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        inWindow = set()

        for r in range(len(s)):

            # close window until curr el is in Window
            while s[r] in inWindow:
                inWindow.remove(s[l])
                l += 1
            
            # open window to add element to inWindow
            inWindow.add(s[r])

            res = max(res, r - l + 1)

        return res


        