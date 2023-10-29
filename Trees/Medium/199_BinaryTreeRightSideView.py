# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        queue = [root]
        while queue:
            lenQ = len(queue)
            lvl = []
            for i in range(0, lenQ):
                curr_node = queue.pop(0)
                if curr_node:
                    lvl.append(curr_node.val)
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
            if lvl:
                right_side_view.append(lvl[-1])
        return right_side_view
