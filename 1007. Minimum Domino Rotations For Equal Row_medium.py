import collections
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        check = A + B
        nums = collections.Counter(check)
        target = max(nums, key=nums.get)
        numa = A.count(target)
        numb = B.count(target)
        for i in range(len(A)):
            if A[i]!= target and B[i] != target:
                return -1
        return len(A) - max(numa,numb)