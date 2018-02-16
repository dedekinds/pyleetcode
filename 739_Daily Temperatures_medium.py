'''
739. Daily Temperatures
2018.2.16
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #http://blog.csdn.net/fuxuemingzhu/article/details/79285081
        save={}
        ans=[]
        for day in range(len(temperatures)-1,-1,-1):
            temp=temperatures[day]
            save[temp]=day
            
            temp_ans=0xfffffff
            for i in range(temp+1,101):
                if i in save and save[i]-day<temp_ans:
                    temp_ans=save[i]-day
            if temp_ans==0xfffffff:
                ans.append(0)
            else:
                ans.append(temp_ans)
        return ans[::-1]
                    