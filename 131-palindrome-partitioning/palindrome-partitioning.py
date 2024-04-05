class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        current = []
        ans = []
        def backtracking(word, left, right):
            
            if left == len(word) or right>len(word) :
                if len(''.join(current)) == len(word):
                    ans.append(current.copy())
                return

            first = word[left:right]

            if first == first[::-1] and len(first) >0:
                current.append(first)
                backtracking(word, right ,right+1 )
                current.pop()

            backtracking(word,left,  right + 1)
        backtracking(s,0,0)
        return ans
        

            