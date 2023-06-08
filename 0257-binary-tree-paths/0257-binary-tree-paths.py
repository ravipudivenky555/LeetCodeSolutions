# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]
        def path(root,s):
            if not(root.left or root.right):
                l.append(s+str(root.val))
                return
            if root.left:
                path(root.left,s+str(root.val)+'->')
            if root.right:
                path(root.right,s+str(root.val)+'->')
        if root:path(root,'')
        return l