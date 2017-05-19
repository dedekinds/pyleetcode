'''448.Find All Numbers Disappeared in an Array
   2017.5.19
   602ms
   beats 3.2%
'''
#不消耗额外的空间，且时间复杂度为O(n)!快的答案不对的
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        #print(nums)
        for x in range(len(nums)):
            #print(x)
            if nums[x]<1:
                continue
            else:
                while(nums[x]>0):
                    if nums[nums[x]-1]<1:
                        nums[nums[x]-1]-=1
                        nums[x]=0
                        #print(nums)
                    else:
                        temp=nums[x]
                        nums[x]=nums[nums[x]-1]
                        nums[temp-1]=-1
        t=0
        for x in nums:
            t+=1
            if x==0:
                ans.append(t)
        return ans
        #http://m.blog.csdn.net/article/details?id=46835507看最下面，这是对数组进行统计             

nums=[4,3,2,7,8,2,3,1]
temp=Solution()
print(temp.findDisappearedNumbers(nums))






#这是不是说明了空间能换时间，但是下面的解答都不满足要求的
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [False]*len(nums)
        
        for num in nums:
            arr[num-1] = True
        
        return [i+1 for i in xrange(len(arr)) if not arr[i]]





class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        check = [0]*len(nums)
        for i in nums:
            check[i-1] += 1
        for j in range(len(check)):
            if check[j] == 0:
                ret.append(j+1)
        return ret
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        #print(nums)
        for x in range(len(nums)):
            #print(x)
            if nums[x]<1:
                continue
            else:
                while(nums[x]>0):
                    if nums[nums[x]-1]<1:
                        nums[nums[x]-1]-=1
                        nums[x]=0
                        #print(nums)
                    else:
                        

                        #temp=nums[nums[x]-1]直接赋值在python里面是药丸的要用copy
                        temp=nums[nums[x]-1]
                        #nums[nums[x]-1]=-1#用[3,2,3]为案例思考一下为啥这两行，且这行不能先运行
                        #nums[x]=temp
                        nums[x]=temp
                        nums[nums[x]-1]=-1#这样也不行，nums[x]已经改变了
                        #print(nums)
        t=0
        for x in nums:
            t+=1
            if x==0:
                ans.append(t)
        return ans
        #http://m.blog.csdn.net/article/details?id=46835507看最下面，这是对数组进行统计             

nums=[1,1]
temp=Solution()
print(temp.findDisappearedNumbers(nums))
'''