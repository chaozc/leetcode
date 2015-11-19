# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def dfs(self, parent, root, lORr):
        if lORr == -1 and parent.right != None:
            root.next = parent.right
        else:
            j = parent.next
            while j != None and j.left == None and j.right == None:
                j = j.next
            if j != None:
                if j.left != None:
                    root.next = j.left
                else:
                    root.next = j.right
        if root.right != None:
            self.dfs(root, root.right, 1);
        if root.left != None:
            self.dfs(root, root.left, -1);
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root != None:
            if root.right != None:
                self.dfs(root, root.right, 1);
            if root.left != None:
                self.dfs(root, root.left, -1);