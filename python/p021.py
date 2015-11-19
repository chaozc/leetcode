# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        p = h
        while l1 != None or l2 != None:
            if l2 == None:
                p.next = l1
                l1 = l1.next
                p = p.next
                continue
            if l1 == None:
                p.next = l2
                l2 = l2.next
                p = p.next
                continue
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
                continue
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
                continue
        h = h.next
        return h