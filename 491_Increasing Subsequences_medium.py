'''
491. Increasing Subsequences
2018.3.6
'''
class Solution(object):
    def findSubsequences(self, nums):
        if len(nums)==0:return []
        temp=set()
        #temp.add([nums[0]])
        temp.add((0xfffffffff,))
        for x in nums:
            for y in list(temp):
                print(y[-1])
                if x>=y[-1]:
                    temp.add(y+(x,))
            temp.add((x,))
        return list( x for x in temp if len(x)>1)
#思路：http://blog.csdn.net/liuchenjane/article/details/54987787


'''
#——————纯暴力————————————
import itertools
class Solution(object):
    def findSubsequences(self, nums):
        ret = []
        for i in range(2, len(nums) + 1):
            ret.extend(set(itertools.combinations(nums, i)))
        return [x for x in ret if self.isIncreasing(x)]

    def isIncreasing(self, l):
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                return False
        return True

'''
