# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, vparent, fparent, root):
        if vparent+1 == root.val:
            f = fparent+1;
        else:
            f = 1
        self.ans = max(self.ans, f);
        if root.left != None:
            self.dfs(root.val, f, root.left);
        if root.right != None:
            self.dfs(root.val, f, root.right);
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.ans = 1;
        self.dfs(root.val-1, 0, root);
        return self.ans