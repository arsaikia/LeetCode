class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = collections.deque([])
        while deck:
            if ans:
                ans.appendleft(ans.pop())
            ans.appendleft(deck.pop())

        return ans