# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """


        if not root:
            return []
        if not (root.left or root.right):
            if root.val == sum:
                return [[root.val]]
        tl = []
        tr = []
        if root.left:
            tl = self.pathSum(root.left, sum-root.val)
        if root.right:
            tr = self.pathSum(root.right, sum-root.val)
        ans = []
        for it in tl+tr:
            ans.append([root.val]+it)
        return ans