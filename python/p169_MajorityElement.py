class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        cnt = 0
        mj = 0
        for n in num:
            if cnt == 0:
                cnt += 1
                mj = n
            else:
                if mj == n:
                    cnt += 1
                else:
                    cnt -= 1
        return mj