# -*- coding:utf-8 -*-
class Solution:
    def find_right(self,data,k,left,right):
        while left <= right:
            mid = left + ((right - left)>>1)
            if data[mid] > k:
                right = mid - 1
            if data[mid] < k:
                left = mid + 1
            if data[mid] == k:
                if mid == len(data) -1:
                    return mid    ###【1,3，3，3】处理左边为要求值的情况,否则mid +1 会越界
                elif data[mid] != data[mid+1]:
                    return mid
                left = mid + 1
        return -1
    def find_left(self,data,k,left,right):
        while left <= right:
            mid = left + ((right - left)>>1)
            if data[mid] > k:
                right = mid - 1
            if data[mid] < k:
                left = mid + 1
            if data[mid] == k:
                if mid == 0:   ###【3,3，3，4】处理左边为要求值的情况,否则mid -1 会越界
                    return mid
                elif data[mid] != data[mid-1]:
                    return mid
                right = mid - 1
        return -1
    def GetNumberOfK(self, data, k):
        # write code here
        temp1 = self.find_left(data,k,0,len(data)-1)
        temp2 = self.find_right(data,k,0,len(data)-1)
        if temp1 == -1 or temp2 == -1:
            return 0
        return temp2 - temp1 +1
        
        
        
        
        
        
        
        
        