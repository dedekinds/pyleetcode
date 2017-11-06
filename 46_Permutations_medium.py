'''
46. Permutations 
2017.11.6
'''

——————————————————————————————————————————
字典序法（缺点是必须从最小字典序开始迭代）
http://www.cnblogs.com/pmars/p/3458289.html

【例】 如何得到346987521的下一个
    1，从尾部往前找第一个P(i-1) < P(i)的位置
            3 4 6 <- 9 <- 8 <- 7 <- 5 <- 2 <- 1
        最终找到6是第一个变小的数字，记录下6的位置i-1
    2，从i位置往后找到最后一个大于6的数
            3 4 6 -> 9 -> 8 -> 7 5 2 1
        最终找到7的位置，记录位置为m
    3，交换位置i-1和m的值
            3 4 7 9 8 6 5 2 1
    4，倒序i位置后的所有数据
            3 4 7 1 2 5 6 8 9
    则347125689为346987521的下一个排列


import math
def find_inverse(nums):#从尾部开始找p[i-1]<P[i]
    temp=nums[::-1]
    for x in range(len(nums)-1):
        if temp[x]>temp[x+1]:
            return len(nums)-x-1    
    return -10

def find_last_max(nums,i,a):#从i开始找，找最后一个大于P[I-1]的位置m
    #ans=-10000
    for x in range(i,len(nums)):
        if nums[x]-a>0:
            ans=x
    return ans
    
class Solution(object):   
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)#必须以最小字典序开始
        res=[]
        t=1
        while t<=math.factorial(len(nums)):
            res.append(nums[:])
            i=find_inverse(nums)
            if i==-10:
                break
            m=find_last_max(nums,i,nums[i-1])

            temp=nums[i-1]
            nums[i-1]=nums[m]
            nums[m]=temp
            
            nums=nums[:i]+nums[i:][::-1]
            t+=1
            
        return res


_____________________________________________________
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