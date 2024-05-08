class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScores = [ (val, idx) for idx, val in enumerate(score)]
        sortedScores.sort(key = lambda x : -x[0])
        
        res = [0] * len(score)

        for i, v in enumerate(sortedScores):
            val, idx = v
            if i == 0:
                score[idx] = "Gold Medal"
            elif i == 1:
                score[idx] = "Silver Medal"
            elif i == 2:
                score[idx] = "Bronze Medal"
            else:
                score[idx] = str(i + 1)
        
        return score
        