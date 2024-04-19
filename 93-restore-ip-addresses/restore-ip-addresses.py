class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(s):
            if len(s) > 3:
                return False
            
            if len(s) > 1 and s[0] == "0":
                return False

            if int(s) in range(0, 256):
                return True
            
            return False

        res = []

        def backtrack(i, ip):

            if i >= len(s):
                if "".join(ip) == s and len(ip) == 4:
                    res.append(".".join(ip))
                return
            
            for j in range(i, len(s)):
                currIp = s[i : j + 1]
                ip.append(currIp)
                if isValid(currIp):
                    backtrack(j + 1, ip)
                ip.pop()
        
        backtrack(0, [])

        return res