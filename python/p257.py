class Solution(object):
    def search(self, root):
        if root.left == None and root.right == None:
            return [str(root.val)]
        ans = []; pre = str(root.val)+"->"
        if root.left != None:
            ansl = self.search(root.left)
            for it in ansl:
                ans.append(pre+it)
        if root.right != None:
            ansr = self.search(root.right)
            for it in ansr:
                ans.append(pre+it)
        return ans
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        return self.search(root)