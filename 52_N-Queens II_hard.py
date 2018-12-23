class Solution(object):
    def is_ok(self,nums,index):
        for i in range(index):
            if nums[i] == nums[index] or abs(nums[i] - nums[index]) == abs(i-index):
                return False
        return True
    
    def queen(self,nums,index):
        if index == len(nums):
            self.res += 1
            return 
        for i in range(len(nums)):
            nums[index] = i
            if self.is_ok(nums,index):
                self.queen(nums,index + 1)
        
    def totalNQueens(self, n):
        self.res = 0
        self.queen([-1]*n,0)
        return self.res
        

https://www.cnblogs.com/bigmoyan/p/4521683.html