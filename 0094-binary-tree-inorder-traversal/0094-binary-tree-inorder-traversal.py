# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        res=[]
        stk=[root]
        tmp=root.left
        while stk or tmp:
            if tmp:
                stk.append(tmp)
                tmp=tmp.left
            else:
                tmp=stk.pop()
                res.append(tmp.val)
                tmp=tmp.right
        return res