这种题还是用STL吧

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        temp_res = s.split()
        if not temp_res:
            return s
        return ' '.join(temp_res[::-1])