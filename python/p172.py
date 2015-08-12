class Solution:
    # @return an integer
    # count how many factor v in n!
    def count(self, n, v):
        ans = 0
        k = v
        while n >= k:
            ans += n/k
            k *= v
        return ans
    def trailingZeroes(self, n):
        return self.count(n, 5)