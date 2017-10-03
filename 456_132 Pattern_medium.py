'''456. 132 Pattern 
   2017.10.3
'''
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        http://www.cnblogs.com/fcyworld/p/6160687.html
        i<j<k
        ai<ak<aj
        """
        ak=-pow(2,33)#存目标三元组中可能的第二大的数
        temp_aj=[]#存最大的那些数，其中最左端的是最大的数
        while nums:
            temp=nums.pop()
            if temp<ak:
                return True
            while temp_aj and temp>temp_aj[-1]:
                ak=temp_aj.pop()
            temp_aj.append(temp)
        return False

    
        
        
'''
想起了下面这个定理（虽然无关）
Erdos Szekeres定理断言，
对任意长度为nm+1的数列{ai}，必有一个长度为n+1的单调不减数列或者一个长度为m+1的单调不升数列
'''