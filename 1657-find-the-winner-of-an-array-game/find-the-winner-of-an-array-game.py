class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
       
        left = arr[0]
        flips = 0
        for r in range(1, len(arr)):
            right = arr[r]
            if right > left:
                arr[0], arr[r] = arr[r], arr[0]
            
            if left == arr[0]:
                flips += 1
            else:
                flips = 1
                left = arr[0]
            
            if flips == k:
                return arr[0]
        
        return arr[0]
        