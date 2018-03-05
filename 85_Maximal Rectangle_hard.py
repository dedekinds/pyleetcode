'''
85. Maximal Rectangle
2018.3.5
'''
'''
本问题是2D→1D：
http://chuansong.me/n/400873436742
http://blog.csdn.net/doc_sgl/article/details/11832965
遍历每一行，若起点为0那么不管，如果为1那么看连着的1有多少个，这样就转换为1D问题了，把每一行都扔进1D问题中即可【O(n^3)？？可以降为O(n^2)】

若3D问题的话http://chuansong.me/n/402433636562
我们可以对它的高从1开始往上切片，如果高于给定的高度设为1，否则设为0，那么变成2D面积问题（注意要乘上高），全过程是O(n^3)

'''
class Solution:
    def one_dim(self,nums):
        if len(nums)==0:return 0
        nums.append(-1)
        stack=[]
        i=0
        ans=0
        while i<len(nums):
            if not stack or nums[stack[-1]]<nums[i]:
                stack.append(i)
                i+=1
            else:
                top=stack.pop()
                if not stack:
                    ans=max(ans,nums[top]*i)
                else:
                    ans=max(ans,nums[top]*(i-stack[-1]-1))
        return ans
            
        
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        nums=[0]*len(matrix[0])#http://blog.csdn.net/doc_sgl/article/details/11832965
        ans=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':
                    nums[j]=0
                else:
                    nums[j]+=1
            ans=max(ans,self.one_dim(nums))
        return ans
        
        
        