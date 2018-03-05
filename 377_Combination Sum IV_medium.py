'''
377. Combination Sum IV
2018.3.5
'''
class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp=[0]*(target+1)
        dp[0]=1
        for x in range(target+1):
            for y in nums:
                if x+y<=target:
                    dp[x+y]+=dp[x]
        return dp[target]
    
    '''
    若(1, 1, 2)(1, 2, 1)算同一类的话
    问题实际上就是一个对nums的 加权和，即sum a_i\cdot nums[i]=K的问题（518. Coin Change 2）
    若a_i={0,1}，那么问题为（494. Target Sum）
    
    '''