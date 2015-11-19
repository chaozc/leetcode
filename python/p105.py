# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bt(self, i1, j1, i2, j2):
        root = TreeNode(self.preorder[i1])
        if j1-i1 == 0:
            return root
        pos = self.inorder.index(root.val)
        root.left = self.bt(i1+1, i1+pos-i2, i2, pos-1) if pos > i2 else None
        root.right = self.bt(i1+pos-i2+1, j1, pos+1, j2) if pos < j2 else None
        return root
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        if preorder == []:
            return None
        
        return self.bt(0, len(preorder)-1, 0, len(preorder)-1)