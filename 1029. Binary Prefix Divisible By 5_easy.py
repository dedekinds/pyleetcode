class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        ans = []
        s = 0
        for i in range(len(A)):
            s = s*2 + A[i]
            ans.append(s%5==0)
        return(ans)