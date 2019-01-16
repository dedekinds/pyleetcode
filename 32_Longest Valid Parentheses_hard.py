设d[i]为以s[i]结尾的最长连续合法串的长度，那么s[i]必定为')'
那么只有两种情况
1.最后两位为 ()，此时容易d[i] = d[i-2] +2
2.最后两位为))，此时....( .....))若s[i-d[i-1]-1]=='('才有希望，

此时d[i] = d[i-1] + d[i-d[i-1]-2]+2
即使d[i-1]=0，也成立


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:return 0
        dp = [0] * (len(s))
        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = [dp[i-2] + 2,2][i-2 < 0]
                else:
                    if i - dp[i-1] -1  >=0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + [dp[i -dp[i-1]-2] + 2, 2][i - dp[i-1]-2 < 0]
        print(dp)
        return max(dp)
        


————————————————————————————————————————————————————————


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        maxLen = 0
        for i,par in enumerate(s):
            if par=='(':
                stack.append(i)
            else:
                try:
                    stack.pop()
                    maxLen = max(maxLen, i-stack[-1])
                except:
                    stack.append(i)
        return maxLen