class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        one = [0] * (amount + 1)
        two = [0] * (amount + 1)
        one[0], two[0] = 1, 1

        for i in range(len(coins)):
            coin = coins[i]

            for j in range(1, len(one)):
                left = 0
                if j >= coin:
                    left = two[j - coin]
                
                top = one[j]
                two[j] = left + top
            one = two
            two = [0] * (amount + 1)
            two[0] = 1
        
        return one[-1]

