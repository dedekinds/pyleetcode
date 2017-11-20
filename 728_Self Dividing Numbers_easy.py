'''
728. Self Dividing Numbers 
2017.11.20
'''
a|abc
b|abc
c|abc
等价于lcm(a,b,c)|abc
用最小公倍数法

from functools import reduce
def gcd(a, b):
    r = a % b
    if r:
        return gcd(b, r)
    else:
        return b
#print gcd(13, 6)

def lcm(a, b):
    return a * b / gcd(a, b)
#print lcm(12, 6)

def lcmAll(seq):
    if len(seq)==1:
        return seq[0]
    return reduce(lcm, seq)

#lis = [a for a in range(1, 11)]
#print lcmAll(lis)

class Solution:
    def selfDividingNumbers(self, left, right):
        ans=[]
        for x in range(left,right+1):
            temp=[]
            length=len(str(x))
            nums=x
            t=0
            exist_zero=0
            while t<length:
                
                if nums%10==0:
                    exist_zero=1
                    break
                temp.append(nums%10)
                nums=int((nums-nums%10)/10)
                t+=1
            if len(temp)==0 or exist_zero==1:#temp有可能为空，此时用不了lcm函数（至少两个元
                continue
            if x%lcmAll(temp)==0:
                ans.append(x)
        return ans