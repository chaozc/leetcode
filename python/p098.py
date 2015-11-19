# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBST(self, root):
        if root == None:
            return None, None, True
        rl = self.isBST(root.left)
        if rl[2] == False or (rl[1] != None and rl[1] >= root.val):
            return None, None, False
        rr = self.isBST(root.right)
        if rr[2] == False or (rr[0] != None and rr[0] <= root.val):
            return None, None, False
        mi = rl[0] if root.left != None else root.val
        ma = rr[1] if root.right != None else root.val
        return mi, ma, True
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBST(root)[2]