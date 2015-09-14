#Sort the height from large to small, for each bar, find the closest bars from left and right that taller than it, and calculate the water volume
#lm:leftmost, rm:rightmost
class Solution(object):
    def trap(self, height):
    	length = len(height)
    	tlist = [(i, height[i]) for i in range(length)]
    	tlist.sort(reverse=True, key=lambda x:(x[1], x[0]))
    	flag = [0]*length
    	if length == 0:
    		return 0
    	lm = tlist[0][0]
    	rm = tlist[0][0]
    	ans = 0
    	#print flag, tlist
    	for i in range(length):
    		if flag[tlist[i][0]] == 1:
    			continue
    		lm = min(lm, tlist[i][0])
    		rm = max(rm, tlist[i][0])
    		for j in range(tlist[i][0]-1, lm, -1):
    			if flag[j] == 0:
    				ans += max(0, tlist[i][1]-height[j])
    			else:
    				break
    			flag[j] = 1
    		for j in range(tlist[i][0]+1, rm):
    			if flag[j] == 0:
    				ans += max(0, tlist[i][1]-height[j])
    			else:
    				break
    			flag[j] = 1

    		#print tlist[i][0], lm, rm, ans
        return ans

if __name__ == "__main__":
	a = Solution()
	print a.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])