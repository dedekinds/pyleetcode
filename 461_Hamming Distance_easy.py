'''461. Hamming Distance 
   2017.5.14
   52ms
   beats 24.72%
'''
from functools import reduce
def str2int(s):
    def add(x,y):
        return x*10+y
    def char2num(s):#注意到'13546'是可迭代类型
        dicttemp={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return dicttemp[s]
    return reduce(add,map(char2num,s))

class Solution(object):
    def hammingDistance(self, x, y):
        a=str2int(bin(x)[2:])
        b=str2int(bin(y)[2:])
        num=0
        for x in str(a+b):
            if x=='1':
                num=num+1
        return(num)

'''
The best code
'''
class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')