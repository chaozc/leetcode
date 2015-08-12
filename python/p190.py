class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        v = 1<<31
        ans = 0
        while n > 0:
            ans += (n%2)*v
            n = n>>1
            v /= 2
        return ans