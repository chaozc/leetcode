class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort(reverse=True)
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        return len(citations)