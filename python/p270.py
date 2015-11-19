# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        mind = abs(target-root.val)
        ans = root.val
        node = root
        while node:
            if mind > abs(target-node.val):
                mind = abs(target-node.val)
                ans = node.val
            if target < node.val:
                node = node.left
            else:
                node = node.right
        return ans