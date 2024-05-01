class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        candidateOne, candidateTwo, countOne, countTwo = None, None, 0, 0

        for num in nums:
            if num == candidateOne:
                countOne += 1
            elif num == candidateTwo:
                countTwo += 1
            elif countOne == 0:
                candidateOne = num
                countOne += 1
            elif countTwo == 0:
                candidateTwo = num
                countTwo += 1
            else:
                countOne -= 1
                countTwo -= 1
            
        # second pass
        countOne, countTwo = 0, 0
        for num in nums:
            if num == candidateOne:
                countOne += 1
            if num == candidateTwo:
                countTwo += 1
        
        res = []
        if countOne > len(nums) // 3:
            res.append(candidateOne)
        if countTwo > len(nums) // 3:
            res.append(candidateTwo)
        
        return res