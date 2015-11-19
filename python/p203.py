# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None and head.val == val:
            head = head.next
        if head != None:
            p = head.next; pre = head;
            while p != None:
                if p.val == val:
                    pre.next = p.next
                else:
                    pre = p
                p = p.next
        return head