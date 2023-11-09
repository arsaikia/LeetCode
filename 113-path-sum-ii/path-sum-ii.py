# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        self.getPaths(root, [], paths, targetSum)
        return paths
    
    def getPaths(self, node, currPath, paths, targetSum):
        if not node:
            return False
        
        currPath.append(node.val)

        if not node.left and not node.right and targetSum == node.val:
            paths.append(currPath[:])
        else:
            self.getPaths(node.left, currPath, paths, targetSum - node.val)
            self.getPaths(node.right, currPath, paths, targetSum - node.val)
        
        currPath.pop()
        
        

        