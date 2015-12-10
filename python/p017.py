import Queue
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if digits == '':
            return []
        q = Queue.Queue()
        q.put('')
        ans = []
        while not q.empty():
            s = q.get()
            if len(s) == len(digits):
                ans.append(s)
            else:
                c = digits[len(s)]
                for cc in dic[c]:
                    q.put(s+cc)
        return ans