# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:return []
        n = len(A)
        B = [0]*n
        C,D = [0]*n,[0]*n
        C[0]=1
        D[n-1] = 1
        for i in range(1,n):
            C[i] = C[i-1] * A[i-1]
        for i in range(n-2,-1,-1):
            D[i] = D[i+1] * A[i+1]
        for i in range(n):
            B[i] = C[i]*D[i]
        return B
            
            