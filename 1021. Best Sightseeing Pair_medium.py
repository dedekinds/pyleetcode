比较容易找到规律，前缀最大值（index+val

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index_plus_val = []
        for i in range(len(A)):
            index_plus_val.append(i + A[i])
        #print(index_plus_val)
        maxval = [index_plus_val[0]]
        
        for i in range(1,len(A)):
            maxval.append(max(maxval[-1],index_plus_val[i]))
        
        dp = [maxval[0]]
        for i in range(1,len(A)):
            dp.append(max(dp[i-1],maxval[i-1]+A[i]-i))
        return dp[-1]