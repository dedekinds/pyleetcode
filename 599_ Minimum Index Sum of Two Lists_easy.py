'''599. Minimum Index Sum of Two Lists
   2017.5.29
   419ms
   beats 0%
'''
from numpy import *
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        A=set(list1)
        B=set(list2)
        temp=list(A&B)
        tempnum=[0]*len(temp)#存temp的序数和
        if len(temp)==1:
            return temp
        else:
           listA=array(list1)
           listB=array(list2)
           for simnum in range(len(temp)):
               tempnum[simnum]=where(listA==temp[simnum])[0][0]+where(listB==temp[simnum])[0][0]
           #print(tempnum)
           ans=[]
           for anstemp in range(len(tempnum)):
               if tempnum[anstemp]==min(tempnum):
                   ans.append(temp[anstemp])
           return ans