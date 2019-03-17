import numpy as np
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:return 1
        l = 1 - np.array(list(map(int,bin(N)[2:])))
        for i in l:
            if i:
                break
        check = l[i:]
        two = 1
        s = 0
        temp = [int(n) for n in check]

        for j in range(len(check)-1,-1,-1):
            s += two*temp[j]
            two*=2
        return s