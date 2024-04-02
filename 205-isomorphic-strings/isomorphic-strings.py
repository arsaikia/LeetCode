class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        maps = collections.defaultdict(str)

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]

            # Already mapped
            if sChar in maps and maps[sChar] != tChar:
                return False
            
            if sChar not in maps:
                if tChar in maps.values():
                    return False
                
                maps[sChar] = tChar

        return True