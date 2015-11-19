# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self, root, target):
        if root:
            self.inorder(root.left, target)
            if root.val > target:
                return
            else:
                self.small.append(root.val)
            self.inorder(root.right, target)
    def r_inorder(self, root, target):
        if root:
            self.r_inorder(root.right, target)
            if root.val <= target:
                return
            else:
                self.large.append(root.val)
            self.r_inorder(root.left, target)
            
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.large = []
        self.small = []
        self.inorder(root, target)
        self.r_inorder(root, target)
        ans = []
        for _ in range(k):
            if len(self.large) == 0:
                ans.append(self.small.pop())
            elif len(self.small) == 0:
                ans.append(self.large.pop())
            elif abs(self.small[-1]-target) < abs(self.large[-1]-target):
                ans.append(self.small.pop())
            else:
                ans.append(self.large.pop())
        return ans
                