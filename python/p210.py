import Queue
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        follow = [-1 for i in range(numCourses)]
        ind = [0 for i in range(numCourses)]
        nedge = len(prerequisites)
        next = [-1 for i in range(nedge)]
        for (id, e) in enumerate(prerequisites):
            next[id] = follow[e[1]]
            follow[e[1]] = id
            ind[e[0]] += 1
        ans = []
        q = Queue.Queue()
        for i in range(numCourses):
            if ind[i] == 0:
                q.put(i)
        while not q.empty():
            i = q.get()
            ans.append(i)
            k = follow[i]
            while k >= 0:
                j = prerequisites[k][0]
                ind[j] -= 1
                if ind[j] == 0:
                    q.put(j)
                k = next[k]
        if len(ans) == numCourses:
            return ans
        return []