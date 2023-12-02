# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs - breadth first search

        res = []

        queue = [root]

        while queue:
            cur_lvl = []

            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    cur_lvl.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if cur_lvl:
                res.append(cur_lvl)
        
        return res
