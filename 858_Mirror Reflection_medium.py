见稍后知乎分析
向上不断翻折，注意上方两个顶点的交替变化
class Solution(object):
    def gcd(self,a,b):
        if b==0:return a
        return self.gcd(b,a%b)
    
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        x = int(q/self.gcd(p,q))
        #print(x)
        if x%2==0:return 0
        else:
            if int(x*p/q)%2 == 0:return 2
            else:return 1
        