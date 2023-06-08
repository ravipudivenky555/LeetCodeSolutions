# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.left==None or root.right==None:
            return 1+self.minDepth(root.right) if root.right else 1+self.minDepth(root.left)
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1