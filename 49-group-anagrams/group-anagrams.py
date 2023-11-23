class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            wordCode = [0 for __ in range(26)]
            for char in word:
                charCode = ord(char) - ord("a")
                wordCode[charCode] += 1
            
            anagrams[tuple(wordCode)].append(word)
        
        return anagrams.values()