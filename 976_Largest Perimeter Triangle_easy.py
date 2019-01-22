class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxv = -0xfffffffffff
        B = sorted(A,reverse=True)
        for i in range(len(A)-2):
            for j in range(i+1,len(A)-1):
                for k in range(j+1,len(A)):
                    if B[k] <= abs(B[i]-B[j]):break
                    else:
                        if maxv < B[k]+B[i]+B[j]:
                            maxv = B[k] + B[i] + B[j]
                            return maxv
        return 0