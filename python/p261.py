class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        v1 = [-1 for i in range(n*2)]; #v1[i]: the end point of the ith edge
        v2 = [-1 for i in range(n*2)]; #v2[i]: the next edge of the ith edge
        v3 = [-1 for i in range(n)] #v3[i]: the first edge starting from the node i
        if len(edges) != n-1:
            return False
        if len(edges) == 0:
            return True
        for i in range(n-1): 
            v1[i*2] = edges[i][1]
            v2[i*2] = v3[edges[i][0]]
            v3[edges[i][0]] = i*2
            v1[i*2+1] = edges[i][0]
            v2[i*2+1] = v3[edges[i][1]]
            v3[edges[i][1]] = i*2+1
        visited = [False for i in range(n)]
        from_ = [-1 for i in range(n)]
        visited[edges[0][0]] = True
        q = [edges[0][0]]
        l = -1; r = 0
        while l < r:
            l += 1
            node = q[l]
            k = v3[node]
            while k >= 0:
                nnode = v1[k];
                if visited[nnode]:
                    if nnode != from_[node]:
                        return False
                else:
                    from_[nnode] = node
                    visited[nnode] = True
                    q.append(nnode)
                    r += 1   
                k = v2[k]
        return True