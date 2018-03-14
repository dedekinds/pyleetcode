'''
300. Longest Increasing Subsequence
2018.3.14
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for num in nums:
            s, e = 0, len(dp) - 1
            while s <= e:
                m = (s + e) / 2
                if dp[m] < num:
                    s = m + 1
                else:
                    e = m - 1
            if s == len(dp):
                dp.append(num)
            else:
                dp[s] = num
        return len(dp)
    '''
思路是先建立一个空的dp数组，然后开始遍历原数组，对于每一个遍历到的数字，我们用二分查找法在dp数组找第一个不小于它的数字，如果这个数字不存在，那么直接在dp数组后面加上遍历到的数字，如果存在，则将这个数字更新为当前遍历到的数字，最后返回dp数字的长度即可，注意的是，跟上面的方法一样，特别注意的是dp数组的值可能不是一个真实的LIS(不理解)
    '''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)
        for x in range(len(nums)):
            for y in range(x):
                if nums[y] < nums[x]:
                    dp[x] = max(dp[x] ,dp[y]+1)
        return max(dp) if dp else 0
        

