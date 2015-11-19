# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not (root.left or root.right):
            return root.val == sum
        tl = False
        tr = False
        if root.left:
            tl = self.hasPathSum(root.left, sum-root.val)
        if (not tl) and root.right:
            tr = self.hasPathSum(root.right, sum-root.val)
        return tl or tr