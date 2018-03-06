'''
162. Find Peak Element
2018.3.6
'''
#“峰值元素”是指值大于邻居的元素
#所以二分一下随随便找一个峰就好。。。
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        size = len(num)
        return self.search(num, 0, size - 1)
    
    def search(self, num, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return [start, end][num[start] < num[end]]
        mid = (start + end) / 2
        if num[mid] < num[mid - 1]:
            return self.search(num, start, mid - 1)
        if num[mid] < num[mid + 1]:
            return self.search(num, mid + 1, end)
        return mid
        
        
        
        
        
        
        
        #——————————O(n)————————————————————
        return nums.index(max(nums))