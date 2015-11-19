# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dp(self, st, en):
        if st > en:
            return [None]
        if st == en:
            node = TreeNode(st);
            return [node];
        ans = []
        for i in range(st, en+1):
            left = self.dp(st,i-1)
            right = self.dp(i+1,en)
            for l in left:
                for r in right:
                    node = TreeNode(i);
                    node.left = l
                    node.right = r
                    ans.append(node)
        return ans
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dp(1,n)