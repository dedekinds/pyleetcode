遍历N->N/2即可，这是因为从二进制>>右移的角度来看，N/2->0的数值包含在
N->N/2中

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        for i in range(N,N/2,-1):
            if bin(i)[2:] not in S:
                return False
        return True