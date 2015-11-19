# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self, root):
        if root == None:
            return True, 0
        bl, hl = self.height(root.left)
        br, hr = self.height(root.right)
        if bl and br and abs(hl-hr) < 2:
            return True, max(hl, hr)+1
        return False, max(hl, hr)+1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root)[0]