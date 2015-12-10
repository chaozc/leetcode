# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        h = head
        t = head
        round = 1
        i = 1
        p = h.next
        t.next = None
        while p:
            if i == k:
                if round == 1:
                    head = h
                    round += 1
                else:
                    last.next = h
                last = t
                h = p
                t = p
                i = 1
                p = p.next
                t.next = None
            else:
                q = p.next
                p.next = h
                h = p
                p = q
                i += 1
        if i == k:
            if round == 1:
                head = h
                round += 1
            else:
                last.next = h
            return head
        else:
            p = h.next
            h.next = None
            while p:
                q = p.next
                p.next = h
                h = p
                p = q
            if round == 1:
                return h
            else:
                last.next = h
                p = head
                return head