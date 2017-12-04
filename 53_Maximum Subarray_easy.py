'''
53. Maximum Subarray 
2017.12.4
'''
-1 1 2 -5
↓（前面加个0）
0 -1 1 2 -5
↓(连续求和)
0 -1 0 2 -3
↓（最大的减去它之前最小的）
3~ [1,2]
#O(n)
class Solution:
    def maxSubArray(self, nums):
        if len(nums)==1:
            return nums[0]

        nums=[0]+nums#在前面加一个0
        tempsum=0
        premin=0
        ans=-0xffffffff
        for x in range(1,len(nums)):
            if tempsum<premin:#找到之前最小的连续和
                premin=tempsum
            tempsum+=nums[x]
            ans=max(ans,tempsum-premin)
            print(premin)
        return ans


DP
https://discuss.leetcode.com/topic/111681/dp-solutions
_________________________________
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    //DP solutions
    var dp = [];
    dp[0] = nums[0];
    var max = nums[0];
    for(var i = 1;i<nums.length;i++){
        dp[i] = nums[i] + (dp[i-1]>0?dp[i-1]:0);
        max = Math.max(dp[i],max);
    }
    return max;
};