'''343. Integer Break 
   2017.9.24
'''
第一反应就是拆分为2和3的和，这是因为他们的和加起来凑得慢但是乘起来狠多
好像以前MO的时候做过类似的？也许可以用调整法证明？
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        dp = [0] * (n + 1)
        dp[2], dp[3] = 2, 3
        for x in range(4, n + 1):
            dp[x] = max(3 * dp[x - 3], 2 * dp[x - 2])
        return dp[n]