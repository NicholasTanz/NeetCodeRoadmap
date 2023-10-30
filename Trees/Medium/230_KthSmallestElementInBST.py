# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def small(root, res):
            if not root:
                return None
            
            small(root.left, res)
            res.append(root.val)
            small(root.right, res)

        small(root, res)
        return res[k-1]

'''
Iterative Solution:
       n = 0
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
'''
        
