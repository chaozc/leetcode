class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def find(self, nums1, l1, nums2, l2, k):
    	#print nums1, l1, nums2, l2, k
    	if l1 > l2:
    		return self.find(nums2, l2, nums1, l1, k)
    	if l1 == 0:
    		return nums2[k-1]
    	if k == 1:
    		return min(nums1[0], nums2[0])
    	p1 = min(k/2, l1)
    	p2 = k-p1
    	if nums1[p1-1] == nums2[p2-1]:
    		return nums1[p1-1]
    	elif nums1[p1-1] < nums2[p2-1]:
    		return self.find(nums1[p1:], l1-p1, nums2, l2, k-p1)
    	else:
    		return self.find(nums1, l1, nums2[p2:], l2-p2, k-p2)
    def findMedianSortedArrays(self, nums1, nums2):
    	l1 = len(nums1)
    	l2 = len(nums2)
    	if (l1+l2)%2 == 1:
    		return self.find(nums1, l1, nums2, l2, (l1+l2+1)/2)
        else:
        	return (self.find(nums1, l1, nums2, l2, (l1+l2)/2)+self.find(nums1, l1, nums2, l2, (l1+l2)/2+1))/float(2)