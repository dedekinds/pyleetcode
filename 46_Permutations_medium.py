2019.1.20更新
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(begin):
            if begin == length:
                ans.append(nums[:])
            for i in range(begin,length):
                nums[begin],nums[i] = nums[i],nums[begin]
                dfs(begin+1)
                nums[begin],nums[i] = nums[i],nums[begin]
        
        ans = []
        length = len(nums)
        dfs(0)
        return ans

_________________________________________________
class Solution:
    def searchpermutation(self,nums,res,index):
        if index == len(nums):
            if nums not in res:
                res.append(nums[:])######!!!!!!!!!!加nums[:]
                
        for i in range(index,len(nums)):
            temp = nums[index]
            nums[index] = nums[i]
            nums[i] = temp
            
            self.searchpermutation(nums,res,index+1)
            
            temp = nums[index]
            nums[index] =nums[i]
            nums[i] = temp 
    
    def permutation(self, nums):
        res = []
        if len(nums) == 0:return res
        self.searchpermutation(nums,res,0)
        return res
_________________________________________________
'''
46. Permutations 
2017.11.6
'''

【递减进位法】
和递增进位法相比product_permutation相同，但是生成的下一个阶乘数有点不同
0000    abcd    1000    bacd    2000    cabd    3000    dabc
0010    abdc    1010    badc    2010    cadb    3010    dacb
0100    acbd    1100    bcad    2100    cbad    3100    dbac
0110    acdb    1110    bcda    2110    cbda    3110    dbca
0200    adbc    1200    bdac    2200    cdab    3200    dcab
0210    adcb    1210    bdca    2210    cdba    3210    dcba

以上表为例，递增进位是上往下生成 0000→0010....
递减是 0000→1000→2000...
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
    n=0
    #【*】
    while n<length:
        if Factorialnum[n]+1<length-n:#【*】
            Factorialnum[n]+=1
            break
        else:
            Factorialnum[n]=0
            n+=1  
    return Factorialnum#【*】
    
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




——————————————————————————————————————————————————————————————————
Steinhaus–Johnson–Trotter算法

设[a1,a2 ... aN] 每一项都有向左或向右两个移动方向。
1) 初始化所有移动方向向左；
2) 如果移动方向的值比自己小，就可移动，比如 <1 >2 <3, 每个数字前箭头的方向表示该数字的移动方向，3可以移动，2和1不可移动；
3) 移动最大的可以动项，在上面例子中就是数字3；
4) 将所有比移动项大的项方向反转，重复第三步，直到不能移动为止。

import math
#Steinhaus–Johnson–Trotter algorithm
def find_legal_move_loacation(direction,nums):#找到最大的可移动的数的位置
    maxlocation=-10086
    maxnum=-10086
    for x in range(len(nums)):
        if x+direction[x]>-1 and x+direction[x]<len(nums):#合法位置
            if nums[x]>nums[x+direction[x]] and nums[x]>=maxnum:
                maxlocation=x
                maxnum=nums[x]
    return maxlocation

class Solution(object):   
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        direction=[-1]*len(nums)
        nums=sorted(nums)#必须从最小字典序开始
        t=1
        ans=[]
        while t<=math.factorial(len(nums)):
            #print(direction)
            ans.append(nums[:])
            location=find_legal_move_loacation(direction,nums)
            if location==-10086:
                break
        #swap 数值
            temp=nums[location]
            nums[location]=nums[location+direction[location]]
            nums[location+direction[location]]=temp
        #swap 方向
            temp_location=location+direction[location]
            a=direction[temp_location]
            direction[temp_location]=direction[location]
            direction[location]=a

        #更新方向
            for x in range(len(nums)):
                if nums[x]>temp:
                    direction[x]*=-1
            t+=1
        return ans
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
#阶乘数→逆序数→排列数【递增进位法】
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

















_____________________________________________________
C语言版STJ算法
#include<stdio.h>
#include<string.h>
#define N 3

int find_legal_move_loacation(int direction[], int nums[]){
    int maxlocation=-10086;
    int maxnum=-10086;
    int x;
    for(x=0;x<N;x++){
        if(x+direction[x]>-1 && x+direction[x]<N){
            if(nums[x]>nums[x+direction[x]] && nums[x]>=maxnum){
                maxlocation=x;
                maxnum=nums[x];
            }
        }
    }
    return maxlocation;
}


int main(){
    int direction[N];
    int nums[N];
    int k;
    int location;
    int temp;
    int a;
    int temp_location;
    int i;
    for(i=0;i<N;i++)
        nums[i]=i;
    for(i=0;i<N;i++)
        direction[i]=-1;
        //={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1}

    //k=find_legal_move_loacation(direction,nums);
   //printf("%d ",k);
    while(1){
        int j;
        for(j=0;j<N;j++){
            printf("%d",nums[j]+1);
        }
        printf("\n");
        location=find_legal_move_loacation(direction,nums);
        //printf("%d",location);
        if (location==-10086)
            break;
        //swapÊýÖµ
            temp=nums[location];
            nums[location]=nums[location+direction[location]];
            nums[location+direction[location]]=temp;
         //swap ·½Ïò
            temp_location=location+direction[location];
            a=direction[temp_location];
            direction[temp_location]=direction[location];
            direction[location]=a;
         ///¸üÐÂ·½Ïò
            int x;
            for(x=0;x<N;x++){
                if (nums[x]>temp){
                    direction[x]*=-1;
                }
            }
            //t+=1
    }
    return 0;
}

_____________________________________________________
C语言版阶乘数算法
#include<stdio.h>
#include<string.h>
#define N 3
long factorial_iteration(int n){
    int result = 1;

    while(n>1){
        result *= n;
        n--;
    }
    return result;
}

int main(){
    int Factorialnum[N];
    int k;
    int i;
    int t;
    int j;
    int temp;
    int tempnums[N];
    int nums[N];
    for(k=0;k<N;k++)
        Factorialnum[k]=0;
    int n=0;
    for(i=0;i<N;i++)
        nums[i]=i;
    int times=1;
    int total=factorial_iteration(N);


    while(times<=total){

     for(j=0;j<N;j++){
            printf("%d",nums[j]+1);
        }
        printf("\n");

      for(i=0;i<N;i++)
        nums[i]=i;
//生成下一个阶乘数（逆序数）__________________
        n=0;

       while(n<N){
        if (Factorialnum[n]+1<N-n){
            Factorialnum[n]+=1;
            break;
        }
        else{
            Factorialnum[n]=0;
            n+=1;
        }
       }

          //printf("%d",n);___________________________________



      //逆序数→排列数______________________
      i=0;
    while(i<N-1){
        if(Factorialnum[i]==0)
            i+=1;
        else{
          for(j=i+Factorialnum[i];j>i;j--){
                temp=nums[j];
                nums[j]=nums[j-1];
                nums[j-1]=temp;
            }
            //nums=nums[:i]+[t]+nums[i:i+Factorialnum[i]]+nums[1+i+Factorialnum[i]:]
            i+=1;
        }
    }
          //逆序数→排列数______________________



        times+=1;
    }
    //逆序数→排列数


    return 0;
}

