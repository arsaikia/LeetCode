class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordAnarams = collections.defaultdict(list)
        res = []

        for word in strs:
            alphabets = [0] * 26
            for char in word:
                key = ord(char) - ord("a")
                alphabets[key] += 1
            
            wordAnarams[tuple(alphabets)].append(word)
        
        for words in wordAnarams.values():
            res.append(words)
        
        return res