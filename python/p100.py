# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pQ = [p]; qQ = [q];
        i = -1; j = 0;
        while i < j:
            i += 1;
            pi = pQ[i]; qi = qQ[i];
            if (pi == None)-(qi == None) != 0:
                return False;
            if pi != None:
                if pi.val != qi.val:
                    return False
                j += 2;
                pQ.append(pi.left); qQ.append(qi.left);
                pQ.append(pi.right); qQ.append(qi.right);
        return True