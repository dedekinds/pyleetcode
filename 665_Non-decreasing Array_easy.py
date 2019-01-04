'''
A[p-1] < A[p] > A[p+1] < A[p+2]
=====>A[p-1] <= A[p+1] or A[p] <= A[p+2]  
'''
 


class Solution:
    def checkPossibility(self, A):
        p = None
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i
        return p is None or p == 0 or p == len(A)-2 or A[p-1] <= A[p+1] or A[p] <= A[p+2]        
