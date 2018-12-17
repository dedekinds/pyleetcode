有必要最后sorted吗？

# -*- coding:utf-8 -*-
class Solution:
    def finpermutation(self,s,res,ptr):
        if ptr == len(s):
            candi = ''.join(s)
            if candi not in res:
                res.append(''.join(s))

        for i in range(ptr,len(s)):
            temp = s[ptr]
            s[ptr] = s[i]
            s[i] = temp
            
            self.finpermutation(s,res,ptr+1)
            
            temp = s[ptr]
            s[ptr] = s[i]
            s[i] = temp
        
        
    def Permutation(self, ss):
        # write code here
        s = list(ss)
        res = []
        if len(ss) == 0:return res
        self.finpermutation(s,res,0)
        return sorted(res)