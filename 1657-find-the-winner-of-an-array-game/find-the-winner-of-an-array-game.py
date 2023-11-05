class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
       
        left = arr[0]
        winstreak = 0
        for r in range(1, len(arr)):
            right = arr[r]
            if right > left:
                arr[0], arr[r] = arr[r], arr[0]
            
            if left == arr[0]:
                winstreak += 1
            else:
                winstreak = 1
                left = arr[0]
            
            if winstreak == k:
                return arr[0]
        
        # when k > len(nums), we take the largest in the arr
        return arr[0]
        