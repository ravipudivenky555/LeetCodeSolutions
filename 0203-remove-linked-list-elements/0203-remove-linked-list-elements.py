# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        t=head
        while head and head.val==val:
            head=head.next
        while t.next:
            if t.next.val==val:
                t.next=t.next.next
            else:
                t=t.next
        return head