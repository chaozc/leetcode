# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search(self, root):
        if root.left == None and root.right == None:
            return str(root.val)
        ans = []
        if root.left != None:
            ansl = self.search(root.left)
            for it in ansl:
                ans.append(str(root.val)+it)
        if root.right != None:
            ansr = self.search(root.right)
            for it in ansr:
                ans.append(str(root.val)+it)
        return ans
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            anslist = self.search(root)
            ans = 0
            for it in anslist:
                ans += int(it)
            return ans