# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validateBST(node, leftLIM, rightLIM):
            if not node:
                return True
            if(node.val > leftLIM and node.val < rightLIM):
                return validateBST(node.left, leftLIM, node.val) and validateBST(node.right, node.val, rightLIM)
            return False
        
        return validateBST(root, float('-inf'), float('inf'))
