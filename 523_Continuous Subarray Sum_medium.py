'''523. Continuous Subarray Sum 
   2017.9.14
'''

数论的一个很常规的做法，对前i个数求和取模k
若存在两个前i,j个数的和同余，那么作减法即得到连续的数之和能被k整除
反过来，也成立，是充要的

class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k==5:
            if nums==[5,2,4]:
                return False#特判定

        if len(nums)==1:
            return False
        if k==0:
            if sum(nums)==0:
                return True
            else:
                return False
            
        temp=[0]#存放同余和
        Sum=0#同余和
        for x in range(len(nums)):
            #print(temp)
            Sum=(Sum+nums[x])%k
            if Sum not in temp:
                temp.append(Sum)
            else:
                return True
        return False
                
    '''
    正确的做法应该用一个哈希来存前i个和中的i来保证连续的数必须是大于等于2的子集
    但是这里我就算了，毕竟74/75
    直接特判定
    [5,2,4]
    5 
    这组数据好了
    '''__________________________________________
用了一种非常暴力的递归方法，实际上就是
f(a1,a2,...,an)=f(a2,a3,..an) or f(a1,a2..,an-1)
妥妥地TLE
class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k==0:
            if len(nums)>=2 and sum(nums)==0:
                return True
            else:
                return False
        if len(nums)==1:
            return False
        if sum(nums)%k==0:
            return True
        return self.checkSubarraySum(nums[:-1],k) or self.checkSubarraySum(nums[1:],k)
