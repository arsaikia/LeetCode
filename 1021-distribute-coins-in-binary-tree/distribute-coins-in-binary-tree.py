# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return (0, 0)   # (treeSize, extraCoins)
            
            leftSize, leftCoins = dfs(node.left)
            rightSize, rightCoins = dfs(node.right)

            size = 1 + leftSize + rightSize
            coins = node.val + leftCoins + rightCoins

            res += abs(size - coins)
            return (size, coins)
        
        dfs(root)
        return res
        