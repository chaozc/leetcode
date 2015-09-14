# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    
    def addTwoNumbers(self, l1, l2):
        headNode = ListNode(0)
        lastNode = headNode
        re = 0
    	while l1 != None and l2 != None:
    		num = re+l1.val+l2.val
    		re = num/10
    		node = ListNode(num%10)
    		node.next = None
    		lastNode.next = node
    		lastNode = node
    		l1 = l1.next
    		l2 = l2.next
    	l = None
    	if l1 != None:
    		l = l1
    	if l2 != None:
    		l = l2
    	while l != None:
    		num = re+l.val
    		re = num/10
    		node = ListNode(num%10)
    		node.next = None
    		lastNode.next = node
    		lastNode = node
    		l = l.next
    	if re > 0:
    		node = ListNode(re)
    		node.next = None
    		lastNode.next = node
    		lastNode = node
        return(headNode.next)