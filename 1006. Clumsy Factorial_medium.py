class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """

        if N==4:
            return N*(N-1)//(N-2)+(N-3)
        if N==3:
            return N*(N-1)//(N-2)
        if N==2:
            return N*(N-1)
        if N ==1:
            return N
        
        ans = [N*(N-1)//(N-2)+(N-3)]
        for i in range(N-4,-1,-4):
            if i - 3>0:
                ans.append(-1 * (i*(i-1)//(i-2))+(i-3))
            else:
                break
        s = sum(ans)
        les = N%4
        print(les)
        if les == 3:
            s = s - les*(les-1)//(les-2)
        if les == 2:
            s =s -les*(les-1)
        if les == 1:
            s =s-les
        return s
        