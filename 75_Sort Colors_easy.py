'''75. Sort Colors 
   2017.6.10
   46ms
'''
#荷兰国旗问题
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = [0]*nums.count(0) + [1]*nums.count(1) + [2]*nums.count(2)
 #有种做法是遍历下去，如果是0那么和首位交换，如果是1那么不动，如果是2那么和尾部交换