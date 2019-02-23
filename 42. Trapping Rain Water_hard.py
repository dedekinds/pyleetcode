

注意到，每个矩形条上方所能接受的水的高度，是由它左边最高的矩形，和右边最高的矩形决定的。
具体地，假设第 i 个矩形条的高度为 height[i]，且矩形条左边最高的矩形条的高度为 left_max[i]，
右边最高的矩形条高度为 right_max[i]，则该矩形条上方能接受水的高度为 
min(left_max[i], right_max[i]) - height[i]。
需要分别从左向右扫描求 left_max，从右向左求 right_max，最后统计答案即可。


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0
        
        left_max = []
        right_max = []
        lm = height[0]
        rm = height[-1]
        
        for i in range(len(height)):
            left_max.append(lm)
            if lm <= height[i]:
                lm = height[i]
        for i in range(len(height)-1,-1,-1):
            right_max.append(rm)
            if rm <=height[i]:
                rm = height[i]
        right_max = right_max[::-1]
        
        res = 0
        for i in range(len(height)):
            if left_max[i]>=height[i] and height[i]<=right_max[i]:
                res += min(left_max[i],right_max[i])-height[i]
        return res
            