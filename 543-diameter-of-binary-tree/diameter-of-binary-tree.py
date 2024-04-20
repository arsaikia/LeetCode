# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        def dfs(node):
            if not node:
                return (0, 0)   # (running, maxDia)
            
            leftRunning, leftMax = dfs(node.left)
            rightRunning, rightMax = dfs(node.right)

            currRunning = 1 + max(leftRunning, rightRunning)
            currMax = max(currRunning, leftRunning + rightRunning + 1, leftMax, rightMax)
            return (currRunning, currMax)
        
        __, maxDia = dfs(root)
        return maxDia - 1
        