class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = [0] * 2001
        for i in arr: m[i+1000] += 1
        vs = [i for i in m if i]
        return len(set(vs)) == len(vs)