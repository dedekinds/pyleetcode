class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A)<=1:return A
        left = 0
        right = len(A)-1
        while left <= right and left>=0 and right<=len(A)-1:
            while left <= right and left>=0 and right<=len(A)-1:
                if A[left] % 2 == 1:
                    break
                left += 1
            while left <= right and left>=0 and right<=len(A)-1:
                if A[right] % 2 == 0:
                    break
                right -= 1
            if left <= right and left>=0 and right<=len(A)-1:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
                left += 1
                right -= 1
        return A
                