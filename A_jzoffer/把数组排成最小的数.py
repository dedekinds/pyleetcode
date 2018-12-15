
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