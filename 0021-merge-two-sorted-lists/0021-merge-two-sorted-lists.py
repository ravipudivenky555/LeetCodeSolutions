# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listNode=None
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        if list1.val<list2.val:
            listNode=list1
            list1=list1.next
        else:
            listNode=list2
            list2=list2.next
        listHead=listNode
        while list1 and list2:
            if list1.val<list2.val:
                listNode.next=list1
                list1=list1.next
            else:
                listNode.next=list2
                list2=list2.next
            listNode=listNode.next
        while list1:
            listNode.next=list1
            list1=list1.next
            listNode=listNode.next
        while list2:
            listNode.next=list2
            list2=list2.next
            listNode=listNode.next
        return listHead