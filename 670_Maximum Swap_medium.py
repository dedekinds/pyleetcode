'''
670. Maximum Swap
2018.2.24
'''
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        获得排序序列temp
        从高位开始对比nums和temp，一旦发现不同的话，从nums[i+1]中先找到最大值，如果有多个这样的最大值的话，那么取index较后的最大值，然后交换即可
        """
        nums=map(int , str(num))
        temp=sorted(nums,reverse=True)
        for i in range(len(nums)):
            if nums[i]==temp[i]:continue
            else:
                maxv=max(nums[i+1:])
                j=nums[i+1:][::-1].index(maxv)
                nums[i],nums[len(nums)-1-j]=nums[len(nums)-1-j],nums[i]
                break
        return int(''.join(map(str,nums)))
                
        