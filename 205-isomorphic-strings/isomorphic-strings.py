class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        

        def modifiedString(s):
            strList = []
            seen = {}
            for idx in range(len(s)):
                char = s[idx]
                if char not in seen:
                    seen[char] = idx
                strList.append(str(seen[char]))
                strList.append(" ")

            return "".join(strList)



        
        print(modifiedString(s))
        print(modifiedString(t))

        return modifiedString(s) == modifiedString(t)

