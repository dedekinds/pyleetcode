'''35. Search Insert Position 
   2017.6.9

'''
def binsearch(arr,tar):
    length=len(arr)
    if arr[0]==tar:
        return 0
    if arr[-1]==tar:#两个边界干脆特殊处理好了
        return (length-1)
    left=0
    right=length-1
    if length==2:#解决长度为2的插入情况
        return 1#因为其他情况由上面的句子和主程序包含了
        
    while (left+1 != right):#用这个可以在不存在时，避免死循环
        #这里似乎暴露了一个问题，假设nums=[1,3]维度为2那么都没法进入循环
        #如果只是查找还好，如果是插入就不行了，改一下，维度为1的情况在主函数已经解决
        mid = int(left+(right-left)/2)#二分查找
        if arr[mid]>tar:
            right=mid
        if arr[mid]<tar:
            left=mid
        if arr[mid]==tar:
            return mid
    return left+1 #本来是return -1

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #猜测线性实惠GG的O(n)回卡特殊样例？目测要二分O(logn)
        #先把两边处理了好了
        #思路，二分查找，找到就找到，找不到就扔进入排序？不过这样不都找到位置了吗
        #要不二分查找+二分插入？O(2logn)
        #直接改二分查找最后一句可以一波流？
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        return binsearch(nums,target)