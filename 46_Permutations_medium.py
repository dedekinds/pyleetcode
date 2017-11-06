'''
46. Permutations 
2017.11.6
'''
____________________________________________________________
#阶乘数→逆序数→排列数
#http://www.cnblogs.com/wanxiao/p/3607225.html
import math
#逆序数→排列数
def product_permutation(Factorialnum,nums):
    for i in range(len(nums)-1):
        if Factorialnum[i]==0:
            i+=1
        else:
            t=nums[i+Factorialnum[i]]
            nums=nums[:i]+[t]+nums[i:i+Factorialnum[i]]+nums[1+i+Factorialnum[i]:]
            i+=1
    return nums
                
#生成下一个阶乘数（逆序数）
def plus_one(Factorialnum):
    length=len(Factorialnum)
    Factorialnum=Factorialnum[::-1]
    n=0
    while n<length:
        if Factorialnum[n]+1<=n:
            Factorialnum[n]+=1
            break
        else:
            Factorialnum[n]=0
            n+=1  
    return Factorialnum[::-1]
    
class Solution(object):   
    def permute(self, nums):
        Factorialnum=[0]*len(nums)
        ans=[]
        Factorialnum=plus_one(Factorialnum)
        
        times=1
        total=math.factorial(len(nums))#循环n!次
        while times<=total:
            ans.append(product_permutation(Factorialnum,nums))
            Factorialnum=plus_one(Factorialnum)
            #print(Factorialnum,product_permutation(Factorialnum,nums))
            times+=1
        return ans

_________________暴力递归________________________________________
class Solution(object):   
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==1:
            return [nums]
        ans=[]
        for i in range(len(nums)):
            temp_ans=[[nums[i]] + temp for temp in self.permute(nums[:i]+nums[i+1:])]
            ans=ans+temp_ans
        return ans

______best code____________________________________________

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in range(len(nums)):
            new_res = []
            for j in res:
                for p in range(len(j)+1):
                    r = j[:]
                    r.insert(p, nums[i])
                    new_res.append(r)
            res = new_res
        return res