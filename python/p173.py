# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.path = [];
        while root != None:
            self.path.append(root);
            root = root.left;
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.path != []:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            ans = self.path[-1]
            self.path = self.path[:-1]
            ne = ans.right
            while ne != None:
                self.path.append(ne)
                ne = ne.left
            return ans.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())