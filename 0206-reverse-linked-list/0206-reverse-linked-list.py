# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        l=[]
        t=head
        while t:
            l.append(t)
            t=t.next
        head=l.pop()
        t=head
        while l:
            t.next=l.pop()
            t=t.next
        t.next=None
        return head