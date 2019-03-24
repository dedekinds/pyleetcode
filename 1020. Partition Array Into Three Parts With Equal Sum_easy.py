class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        S = sum(A)
        if S%3 != 0:return False
        part = S//3
        cnt = 0
        temps = 0
        for i in range(len(A)):
            temps += A[i]
            if temps == part:
                cnt += 1
                temps = 0
        return cnt == 3