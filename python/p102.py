# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ans = [[root]];
        level = 0
        while len(ans[level]) > 0:
            ans.append([])
            for node in ans[level]:
                if node.left != None:
                    ans[level+1].append(node.left)
                if node.right != None:
                    ans[level+1].append(node.right)
            level += 1
        ans = ans[:-1]
        return [[node.val for node in nlist] for nlist in ans]