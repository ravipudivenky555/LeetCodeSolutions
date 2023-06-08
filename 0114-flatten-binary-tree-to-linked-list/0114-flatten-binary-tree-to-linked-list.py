# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            temp1=root.left
            temp=root.left
            root.left=None
            while temp1 and temp1.right:
                temp1=temp1.right
            if temp1:
                temp1.right=root.right
                root.right=temp
            root=root.right