# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        dic = {}
        q = Queue.Queue()
        q.put((root, 0))
        mi = 0
        ma = 0
        while not q.empty():
            (node, col) = q.get()
            if not dic.has_key(col):
                dic[col] = []
                mi = min(mi, col)
                ma = max(ma, col)
            dic[col].append(node.val)
            if node.left:
                q.put((node.left, col-1))
            if node.right:
                q.put((node.right, col+1))
        return [dic[i] for i in range(mi, ma+1)]