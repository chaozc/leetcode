# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return []
        qmi = []; qma = [];
        node = head
        while node != None:
            if node.val < x:
                qmi.append(node)
            else:
                qma.append(node)
            node = node.next
        qmi = qmi+qma
        for i in range(1, len(qmi)):
            qmi[i-1].next = qmi[i]
        qmi[-1].next = None
        return qmi[0]