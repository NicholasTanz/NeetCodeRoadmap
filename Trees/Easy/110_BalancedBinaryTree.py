# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True        
        def checkBalance(retBool, root):
            if not root:
                return [True, 0]
            l_side = checkBalance(retBool, root.left)
            r_side = checkBalance(retBool, root.right)
            if(abs(l_side[1] - r_side[1]) <= 1 and retBool and l_side[0] and r_side[0]):
                return [True, 1+max(l_side[1], r_side[1])]
            else:
                return [False, 0]

        return checkBalance(True, root)[0]
