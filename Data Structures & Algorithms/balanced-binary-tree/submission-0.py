# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            diff = left_height - right_height

            # unbalanced node
            if abs(diff) > 1:
                return -1
            if left_height == -1:
                return -1
            if right_height == -1:
                return -1

            return 1 + max(left_height, right_height)
        
        return height(root) != -1
    
            