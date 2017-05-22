'''506_ Relative Ranks 
   2017.5.22
   106ms
   beats 85.09%
'''
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        indexdict={}
        A=sorted(nums)[::-1]
        long=0
        #先搞好第一第二第三名
        length=len(nums)       
        if length==1:
            indexdict[str(A[0])]="Gold Medal"
        if length==2:
            indexdict[str(A[0])]="Gold Medal"
            indexdict[str(A[1])]="Silver Medal"
        if length>=3:   
            indexdict[str(A[2])]="Bronze Medal"
            indexdict[str(A[1])]="Silver Medal"
            indexdict[str(A[0])]="Gold Medal"
            for x in range(3,len(A)):
                indexdict[str(A[x])]=str(x+1)
        #return indexdict
        for y in range(len(nums)):
            nums[y]=indexdict[str(nums[y])]
        return nums 
'''
nums=[10,3,8,9,4]是分数
给出同序的排名如[1,5,3,2,4]然后做个替换
'''     

'''
The best code
42ms
'''
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nl = sorted(nums)[::-1]
        rnk = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums)+1))
        return map(dict(zip(nl,rnk)).get, nums)





dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
dict["w"] = "watermelon"
"Gold Medal", "Silver Medal", "Bronze Medal"