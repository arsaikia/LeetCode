# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.rootWithMaxDia = None

        def getPathWithMaxDiameter( node ):
            if not node:
                return [ [], [] ]   # (running, longest)
            
            leftRunning, leftMax = getPathWithMaxDiameter(node.left)
            rightRunning, rightMax = getPathWithMaxDiameter(node.right)

            if len(leftMax) > len(rightMax):
                longest = leftMax
            else:
                longest = rightMax
            
            if len(leftRunning) + len(rightRunning) + 1 > len(longest):
                longest = leftRunning + [ node.val ] + rightRunning
            
            if len(leftRunning) > len(rightRunning):
                runningMax = leftRunning + [node.val]
            else:
                runningMax = [node.val] + rightRunning

            return (runningMax, longest)
        
        __, longest = getPathWithMaxDiameter( root )

        return len(longest) - 1
            
                
        