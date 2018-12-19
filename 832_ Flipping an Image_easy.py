比较的方法是前后交换的同时变更值，在一次遍历就把问题解决

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A)==0 or len(A[0])==0:return A
        for row in A:
            for i in range(int((len(row)+1)/2)):
                row[i],row[~i] = row[~i]^1,row[i]^1
        return A
    
