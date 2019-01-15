一种比较暴力的方式总时间是O(N)感觉还行，首先是求一个从前往后的连续和并+5 %5保证所有的数都在0-4之间，
然后统计0-4的鄋数的数量，然后分别Cn 2想加起来，0的话另外算，这样就可以了

import collections
class Solution(object):
    def C2(self,num):
        return int(num*(num-1)/2)
    
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A[0] = (A[0]+K)%K
        for i in range(1,len(A)):
            A[i] = (A[i]+A[i-1]+K)%K
        temp = collections.Counter(A)
        ans = 0
        for i in temp:
            if temp[i] > 1:
                ans += self.C2(temp[i])
        return ans + A.count(0)