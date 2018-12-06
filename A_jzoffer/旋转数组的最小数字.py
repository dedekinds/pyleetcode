把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# -*- coding:utf-8 -*-
class Solution:
    def linearsearch(self,rotateArray,start,end):
        temp = rotateArray[start]
        for i in range(start+1,end):
            if rotateArray[i] < temp:
                return rotateArray[i]
        return temp
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:return 0
        start = 0
        end = length - 1
        mid = start
        while (rotateArray[start] >= rotateArray[end]):
            if (end - start) == 1:
                mid = end
                break
            mid = (end + start)>>1
 
            if rotateArray[start] == rotateArray[end] and rotateArray[end] == rotateArray[mid]:
                return self.linearsearch(rotateArray,start,end)
             
            if rotateArray[mid] >= rotateArray[end]:
                start = mid
            else:
                end = mid
        return rotateArray[mid]