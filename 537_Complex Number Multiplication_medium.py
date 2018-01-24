'''
537. Complex Number Multiplication
2018.1.24
'''

class Solution(object):
    def getnums(self,nums):
        #取出实部
        for x in range(len(nums)):
            if nums[x]=='+':
                a=nums[0:x]
                b=nums[x+1:-1]
                break
        
        return int(a),int(b)
    
    def complexNumberMultiply(self, m, n):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a,b=self.getnums(m)
        c,d=self.getnums(n)
        return str(a*c-b*d)+'+'+str(a*d+b*c)+'i'