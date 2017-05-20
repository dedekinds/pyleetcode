'''283_Move Zeroes   
   2017.5.20
   109ms
   beats 27.58%
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        time=0#记录有多少个需要砍掉的0
        length=len(nums)
        for x in nums[0:length]:
            if x == 0:
                time+=1
            else:
                nums.append(x)
        #nums=nums[length:]+[0]*time#似乎这样是不行的，他处理的仅仅是函数里面的nums
        #print(nums)#而非外部的nums，只能用append,pop这样的办法？
        #return nums
        for y in range(length):
            nums.pop(0)
        for z in range(time):
            nums.append(0)

'''
这样的办法对负数无效，但是在C++和JAVA是可以的
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #http://blog.csdn.net/zhongjiekangping/article/details/6855864
        #直到不产生进位为止
        #x^y //执行加法
        #(x&y)<<1 //进位操作
        result=a^b
        while(a&b):
            b=(a&b)<<1
            a=result
            result=a^b
            print(result)
        return result
'''

'''
best code
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """       
        n = len(nums)
        nums[:] = filter(None, nums)
        nums.extend([0] * (n - len(nums)))

'''
错误版本
'''
错误版本1
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        time=0#记录有多少个需要砍掉的0
        length=len(nums)
        for x in nums[0:length]:
            if x == 0:
                time+=1
            else:
                nums.append(x)
        nums=nums[length:]+[0]*time#由于这一步没有返回并不能改变nums
    
nums=[0, 1, 0, 3, 12]
temp=Solution()
print(temp.moveZeroes(nums))
'''

    1.You must do this in-place without making a copy of the array.
    2.Minimize the total number of operations.

'''


错误版本2
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        time=0#记录有多少个需要砍掉的0
        length=len(nums)
        for x in nums[0:length]:
            if x==0:
                nums.append(0)
                time+=1
        #pop导致数组改变，序号对不齐很多错误
        print(nums,time)
        number=0
        for y in nums:
            print(y)
            if y ==0:
                nums.pop(number)
                time-=1
                #print(nums,time,y)
                if time==0:
                    break
                
            number+=1
        return nums
    
nums=[0,0,1]
temp=Solution()
print(temp.moveZeroes(nums))
'''

    1.You must do this in-place without making a copy of the array.
    2.Minimize the total number of operations.

'''