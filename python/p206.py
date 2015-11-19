# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def r(self, head):
        if head.next:
            lasth, last = self.r(head.next)
            last.next = ListNode(head.val)
            return lasth, last.next
        else:
            lasth = ListNode(head.val)
            return lasth, lasth
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            lasth, last = self.r(head)
            return lasth
        return None