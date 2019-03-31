负数进位制问题！！
class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:return '0'
        ans = []
        while N:
            k = N%(-2)
            N = N//(-2)
            if k < 0:
                k -= (-2)
                N += 1
            ans.append(str(k))
        return ''.join(ans[::-1])
        