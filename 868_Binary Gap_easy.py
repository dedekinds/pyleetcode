class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N&(N-1)==0 :return 0
        gap = 0
        while N:
            #find fir
            while N:
                if N&1 == 1:
                    num = 0
                    N = N >> 1
                    break
                else:N = N >> 1
            #find sec
            while N:
                if N&1 == 1:
                    num += 1
                    if gap <= num:
                        gap = num
                    num = 0
                    N = N >> 1
                else:
                    num += 1
                    N = N >> 1
        return gap
                
                