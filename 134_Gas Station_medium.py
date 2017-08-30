'''134. Gas Station 
   2017.8.30
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        else:
            ans=0
            temp=0
            for x in range(len(gas)):
                temp+=gas[x]-cost[x]
                if temp<0:
                    ans=x+1
                    temp=0
            return ans
                
            
'''
http://bookshadow.com/weblog/2015/08/06/leetcode-gas-station/
结论1：若从加油站A出发，恰好无法到达加油站C（只能到达C的前一站）。则A与C之间的任何一个加油站B均无法到达C。
结论2：若储油量总和sum(gas) >= 耗油量总和sum(cost)，则问题一定有解。
'''