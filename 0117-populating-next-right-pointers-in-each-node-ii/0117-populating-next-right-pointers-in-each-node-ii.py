"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        mainqueue=list()
        mainqueue.append(root)
        if root==None:
            return None
        while mainqueue:
            secondqueue=[]
            temp=mainqueue.pop(0)
            if temp.left:
                secondqueue.append(temp.left)
            if temp.right:
                secondqueue.append(temp.right)
            for i in mainqueue:
                if i.left:secondqueue.append(i.left)
                if i.right:secondqueue.append(i.right)
                temp.next=i
                temp=i
            mainqueue=secondqueue
        return root