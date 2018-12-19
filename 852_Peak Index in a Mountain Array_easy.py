二分法，可以看成是A[i]<A[i+1]的比较
true true false false false的第一个true的问题
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:return 0
        left = 0
        right = len(A)-1
        while left < right:
            mid = (left + right) >> 1
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left


        ______


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:return 0
        left = 0
        right = len(A)-1
        while left <= right:
            mid = (left + right) >> 1
            if A[mid] < A[mid+1]:
                left = mid + 1
            if A[mid] > A[mid+1]:
                right = mid - 1
        return left