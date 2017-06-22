'''15. 3Sum 
   2017.6.22

'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        nums=sorted(nums)
        for x in range(len(nums)):#先排序O(nlogn)，然后，遍历每个数，另外用两个
            temp=nums[x]#指针首尾用tow sum的跌跤办法来夹逼，且要遍历完全，一共是O(n2)
            nums.pop(x)
            left=0
            right=len(nums)-1
            while (left<right):
                if nums[left]+nums[right]==-temp:
                    tempans=sorted([temp,nums[left],nums[right]])
                    if tempans in ans:
                        pass
                    else:
                        ans.append(tempans)#哈希存？
                    right-=1
                if nums[left]+nums[right]>-temp:
                    right-=1
                if nums[left]+nums[right]<-temp:
                    left+=1
            nums.insert(x,temp)#似乎两个指针要是碰到
        return ans
        
                
                    

nums=[-1, 0, 1, 2, -1, -4]
temp=Solution()
print(temp.threeSum(nums))

#过了311/313个样例。。然后TLE