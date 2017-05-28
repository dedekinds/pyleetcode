'''453. Minimum Moves to Equal Array Elements   
   2017.5.29
   55ms
   beats 48.94%
'''
#神他妈找规律猜答案AC系列，居然中了
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-min(nums)*len(nums)
#理性思路是对的，但总是WA和TLE，说到底还是太烂了
'''
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #思路是先排列取最小的N-1个数不断+1使得最小的等于最大的，重新排列，如此循环下去
        number=0
        while(len(nums)>1):
            print(nums)
            nums.sort()
            number+=(nums[-1]-nums[0])
            nums.pop()
            nums[-1]+=number
            nums[0]+=number
        return number

#第一个错误，不能一直+1+1的，比如[1,2147483647]
#不能for太长，比如[383,886,777,915,793,335,386,492,649,421,362,27,690,59,763,926,540,426,172,736,211,368,567,429,782,530,862,123,6
     
nums=[5,6,8,8,5]
temp=Solution()
print(temp.minMoves(nums))

'''

需要换一个角度来看问题，其实给n-1个数字加1，
效果等同于给那个未被选中的数字减1，比如数组[1，2，3], 
给除去最大值的其他数字加1，变为[2，3，3]，我们全体减1，
并不影响数字间相对差异，变为[1，2，2]，
这个结果其实就是原始数组的最大值3自减1，那么问题也可能转化为，
将所有数字都减小到最小值