'''
413. Arithmetic Slices
2018.1.31
'''
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #若序列S为等差数列，其长度为N，则其等差数列切片的个数SUM = 1 + 2 + ... + (N - 2)
        if len(A) < 3:
            return 0
        delta=A[1]-A[0]
        ans=0
        cnt=0
        
        for x in range(2,len(A)):
            if A[x]-A[x-1]==delta:
                cnt+=1
                ans+=cnt
            else:
                delta=A[x]-A[x-1]
                cnt=0
        return ans
        