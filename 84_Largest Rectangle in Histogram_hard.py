'''
84. Largest Rectangle in Histogram
2018.3.4
'''
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights)==0:return 0
        heights.append(-1)
        stack=[]
        ans=0
        i=0
        while i<len(heights):
            if not stack or heights[stack[-1]]<=heights[i]:
                stack.append(i)
                i+=1
            else:
                top=stack.pop()
                if not stack:
                    ans=max(ans,heights[top]*i)#空栈的时候说明此时达到了全部的矩形的最小的那个
                else:
                    ans=max(ans,heights[top]*(i-stack[-1]-1))
        return ans

                
                
        
        
        
'''
非常迷的单调栈方法，
1.http://chuansong.me/n/390896436960:最后一幅图的棕色圈有问题似乎
2.http://blog.csdn.net/yutianzuijin/article/details/52072427

def largestRectangleArea(self, height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans
'''