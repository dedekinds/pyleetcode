class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        temp = int(''.join([str(tmp) for tmp in A])) + K
        res = []
        str_res = str(temp)
        for i in str_res:
            res.append(int(i))
        return res