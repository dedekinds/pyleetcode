
!!!!!!!!!!!!!!!!!!!!!!
这样的写法在python3中并不适用
!!!!!!!!!!!!!!!!!!!!!!
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        cmp = lambda s1,s2:int(str(s1)+str(s2)) - int(str(s2)+str(s1))
        array = sorted(numbers,cmp = cmp)
        return ''.join([str(i) for i in array])



!!!!!!!!!!!!!!!!!!!!!!
python3中的写法
!!!!!!!!!!!!!!!!!!!!!!

import functools
def cmp(s1,s2):
    a = str(s1)
    b = str(s2)
    if int(a+b) < int(b+a):
        return -1
    if int(a+b) < int(b+a):
        return 1
    return 0

array = sorted(numbers,key = functools.cmp_to_key(cmp))
return ''.join([str(i) for i in array])

