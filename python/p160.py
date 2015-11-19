# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLen(self, head):
        l = 0
        while head != None:
            head = head.next
            l += 1
        return l
    def go(self, head, k):
        for i in range(k):
            head = head.next
        return head
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        l1 = self.getLen(headA)
        l2 = self.getLen(headB)
        if l1 > l2:
            headA = self.go(headA, l1-l2)
        else:
            headB = self.go(headB, l2-l1)
        while headA != headB:
            headA = headA.next
            headB = headB.next
        if headA == None:
            return 
        else:
            return headA