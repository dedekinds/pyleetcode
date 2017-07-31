
'''119. Pascal's Triangle II 
   2017.7.31
'''
class Solution(object):
    def getRow(self, rowIndex):
        n=0
        Y=[1]
        if rowIndex==0:return Y
        while n<rowIndex:
            Y=[1]+[Y[i-1]+Y[i] for i in range(len(Y)) if i>0]+[1]
            n+=1
        return Y