#keep a stack pos[i], where for i < j, pos[i]<pos[j] h[pos[i]]<h[pos[j]]
#scan from left to right
#for a new height h[i]
#find the leftmost h[pos[k]] where h[pos[k]] < h[i]
#update the answer with the area between pos[j] and i(not include i), where k < j <top, (top: the current size of the stack)
#O(n), maximum:O(2n)(h:1 2 3 4 5 1, O(2n))
class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
        	return 0
        pos = []
        top = -1
        ans = 0
        i = -1
        height.append(0)
        while i < n: 
        	i += 1
        	if top == -1 or height[i] >= height[pos[top]]:
        		top += 1
        		if top == len(pos):
        			pos.append(0)
        		pos[top] = i
        	else:
        		p = pos[top]
        		top -= 1
        		if top < 0:
        			area = i*height[p]
        		else:
        			area = (i-pos[top]-1)*height[p]
        		i = i-1
        		ans = max(ans, area)
        return ans

if  __name__ == "__main__":
	a = Solution()
	print a.largestRectangleArea([2,1,5,6,2,3])