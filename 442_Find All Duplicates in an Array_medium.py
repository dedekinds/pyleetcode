'''442. Find All Duplicates in an Array 
   2017.9.30
'''


——————————————————————————————————————————————————
实际上就是字母统计，采用常规-1交换法，无额外空间+O(n)居然被长样例TLE了
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        pointer=0
        ans=[]
        while pointer<len(nums):
            #print(nums)
            if nums[pointer]<=0:
                pointer+=1
                continue
            else:
                temp=nums[pointer]
                if nums[nums[pointer]-1]<0:
                    nums[pointer]=0
                    ans.append(temp)
                    pointer+=1
                    continue
                else:
                    nums[pointer]=nums[nums[pointer]-1]
                    nums[temp-1]=-1
        return ans
                
