# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None:
            return node
        q = [node]
        new = UndirectedGraphNode(node.label)
        dic = {node.label:new}
        o = new
        i = -1; j = 0
        while i < j:
            i += 1
            nod = q[i]
            new = dic[nod.label]
            for nei in nod.neighbors:
                if not dic.has_key(nei.label):
                    next = UndirectedGraphNode(nei.label)
                    dic[nei.label] = next
                    j += 1
                    q.append(nei)
                next = dic[nei.label]
                new.neighbors.append(next)
        return o