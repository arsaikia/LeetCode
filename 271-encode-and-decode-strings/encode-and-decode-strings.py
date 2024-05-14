class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for word in strs:
            encoded.append(str(len(word)))
            encoded.append("#")
            encoded.append(word)
        
        return "".join(encoded)

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            wordSize = int(s[i : j])
            # word starts at j + 1
            word = s[j + 1 : j + wordSize + 1]
            res.append(word)

            i = j + wordSize + 1

        return res
        

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))