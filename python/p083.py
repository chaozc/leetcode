# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        node = head.next
        last = head
        while node != None:
            if node.val == last.val:
                last.next = node.next
            else:
                last = node
            node = node.next
        return head