'''
661. Image Smoother 
2017.11.22
'''
暴力模拟九宫格模板（速度略慢
def check_legal_location(M,i,j):
    n=len(M)
    m=len(M[0])
    if i>-1 and i<n and j>-1 and j<m:
        return True
    return False
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        temp_ans=[]
        ans=[[0]*len(M[0]) for x in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                if check_legal_location(M,i,j):
                    temp_ans.append(M[i][j])
                    
                if check_legal_location(M,i-1,j):
                    temp_ans.append(M[i-1][j]) 
                    
                if check_legal_location(M,i-1,j-1):
                    temp_ans.append(M[i-1][j-1])  
                    
                if check_legal_location(M,i-1,j+1):
                    temp_ans.append(M[i-1][j+1])
                    
                if check_legal_location(M,i+1,j):
                    temp_ans.append(M[i+1][j])
                    
                if check_legal_location(M,i+1,j-1):
                    temp_ans.append(M[i+1][j-1])
                    
                if check_legal_location(M,i+1,j+1):
                    temp_ans.append(M[i+1][j+1])
                    
                if check_legal_location(M,i,j+1):
                    temp_ans.append(M[i][j+1])  
                    
                if check_legal_location(M,i,j-1):
                    temp_ans.append(M[i][j-1])
                ans[i][j]=int(sum(temp_ans)/len(temp_ans))
                temp_ans=[]
        return ans