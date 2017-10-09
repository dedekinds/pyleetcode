''' 55. Jump Game
   2017.10.8
'''
O(n)的做法，实际上就是看每一步能够得着多远
class Solution(object):
    def canJump(self, nums):
        reach=0
        i=0
        n=len(nums)
        while (i<=reach and i<=n):
            reach=max(reach,nums[i]+i)
            i+=1
            #print(reach)
            if reach>=n-1:
                return True
        return False