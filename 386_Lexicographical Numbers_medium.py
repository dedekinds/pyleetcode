'''386. Lexicographical Numbers 
   2017.9.8
'''
对下面第三种递归办法的一种迭代做法，节省空间（实际上理解上需要好好想想
class Solution(object):
    def lexicalOrder(self, n):
        ans=[]
        stack=[1]
        while stack:
            temp=stack.pop()
            ans.append(temp)
            if temp<n and temp%10<9:
                stack.append(temp+1)
            if temp*10<=n:
                stack.append(10*temp)
        return ans

——————————————————————————————————————————
#排序的办法，对于两个数比如123和56，那么取出等长的‘12’和‘56’
用'12'+'56'和'56'+'12'的大小定义一种排序，可以参考‘179. Largest Number ’
很遗憾TLE

from functools import cmp_to_key
def compare(a,b):
    temp=min(len(a),len(b))
    return [1,-1][a[:temp]+b[:temp]<b[:temp]+a[:temp]]

class Solution(object):
    def lexicalOrder(self, n):
        temp = cmp_to_key(compare)
        nums=list(range(1,n+1))
        #res = ''.join(sorted([str(x) for x in nums], key=temp)).lstrip('0')
        res=sorted([str(x) for x in nums], key=temp)
        return [int(x) for x in res]


——————————————————————————————————————————
一种递归的做法，不过是超空间的
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        def solve(m):
            result.append(m)
            if m * 10 <= n: solve(m * 10)
            if m < n and m % 10 < 9: solve(m + 1)
        solve(1)
        return result