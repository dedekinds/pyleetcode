
'''496. Next Greater Element I  
   2017.7.27

'''
先用stack来做一个map，使得map中的元素指向下一个更大的元素
然后最后用一个get函数就搞定
这里的话是O(m+n)的
如果直接暴力的话，那么就O(mn)
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        temp={}
        stack=[]
        #做一个map，使得map中的元素指向下一个更大的元素
        for x in nums:
            while stack and stack[-1]<x:
                temp[stack.pop()]=x
            stack.append(x)

        #get(n,-1)的意思是找n对应的元素，如果找不到就返回-1
        return [temp.get(n,-1) for n in findNums]