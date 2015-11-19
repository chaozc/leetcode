# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def dfs(self, parent, root, lORr):
        if lORr == -1:
            root.next = parent.right
        else:
            if parent.next != None:
                root.next = parent.next.left
        if root.right != None:
            self.dfs(root, root.right, 1);
            self.dfs(root, root.left, -1);
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root != None and root.right != None:
            self.dfs(root, root.right, 1);
            self.dfs(root, root.left, -1);