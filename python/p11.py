#mi, mo:Find the rightmost and leftmost one that taller than i
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        length = len(height)
        tlist = [(i, height[i]) for i in range(length)]

        tlist = sorted(tlist, key=lambda x:(x[1], x[0]), reverse=True)
        ma = tlist[0][0]
        mi = ma
        ans = 0
        for i in range(1, length):
        	ma= max(ma, tlist[i][0])
        	ans = max(tlist[i][1]*(ma-tlist[i][0]), ans)
        	mi = min(mi, tlist[i][0])
        	ans = max(tlist[i][1]*(tlist[i][0]-mi), ans)
        return ans

if __name__ == "__main__":
	a = Solution()
	print a.maxArea([1,2,4,1,2])