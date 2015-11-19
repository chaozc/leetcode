# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, target, path):
        if root.val == target.val:
            return path
        elif target.val < root.val:
            path.append(root.left);
            return self.dfs(root.left, target, path);
        else:
            path.append(root.right);
            return self.dfs(root.right, target, path);
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1 = self.dfs(root,p,[root]);
        path2 = self.dfs(root,q,[root]);
        l = min(len(path1), len(path2));
        path1 = path1[:l];
        path2 = path2[:l];
        for i in range(l-1, -1, -1):
            if path1[i].val == path2[i].val:
                return path1[i]
        