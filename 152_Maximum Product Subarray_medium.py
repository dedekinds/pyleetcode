在讨论里面看到的神方法：
如果负号为偶数，那么全部乘起来就是最大值
如果负号为奇数，那么最大乘积肯定是从头开始或者从末尾开始的连续乘积（恰好剔除其中一个负号就是了）
如果有0的话，重新隔开0重启就是了
A[i] *= A[i-1] or 1 就是如果A[i-1]!=0: ...否则乘以1

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums
        B = nums[::-1]
        for i in range(1,len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(A+B)

——————————————————————————————————————————————