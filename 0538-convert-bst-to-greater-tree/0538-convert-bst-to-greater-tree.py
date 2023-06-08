# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseInorder(self,root):
        if root==None:
            return None
        if root.right!=None:
            root.right=self.reverseInorder(root.right)
        self.key+=root.val
        root.val=self.key
        if root.left!=None:
            root.left=self.reverseInorder(root.left)
        return root
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.key=0
        return self.reverseInorder(root)